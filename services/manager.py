

from services import data_service
from models.incomes import Income
from models.expenses import Expense
from models.transactions import Transaction


class Manager:
    def __init__(self, limit=50000):
        self.transactions = []
        self.limit = limit
        
        data = data_service.load_transactions()
        for transaction in data:
            try:
                if not isinstance(transaction, dict) or "type" not in transaction or "amount" not in transaction or "date" not in transaction:
                    continue
                
                if transaction["type"] == "income":
                    new_income = Income(transaction["amount"], transaction["date"], transaction.get("source", "general"))
                    self.add_transaction(new_income)
                elif transaction["type"] == "expense":
                    new_expense = Expense(transaction["amount"], transaction["date"], transaction.get("category", "general"))
                    self.add_transaction(new_expense)
                else:
                    continue
            except Exception as e:
                print(f"Skipping invalid transaction: {e}")
                continue
            
                
    
    @property
    def balance(self):
        return sum(t.sign_amount() for t in self.transactions)
    
    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise ValueError("Only Transaction objects can be added")
        
        self.transactions.append(transaction)

    def get_expenses(self):
        return [transaction for transaction in self.transactions if isinstance(transaction, Expense)]

    def get_incomes(self):
        return [transaction for transaction in self.transactions if isinstance(transaction, Income)]

    def get_total_expenses(self):
        amounts = map(lambda expense: self.get_amount(expense), self.get_expenses())
        return sum(amounts)

    def get_total_income(self):
        amounts = map(lambda income: self.get_amount(income), self.get_incomes())
        return sum(amounts)

    def get_category_breakdown(self):
        result = {}

        for expense in self.get_expenses():
            category = expense.category
            amount = expense.amount

            if category in result:
                result[category] += amount
            else:
                result[category] = amount

        return result

    def get_unique_categories(self):
        return {expense.category for expense in self.get_expenses()}

    def get_category_report_rows(self):
        return tuple(sorted(self.get_category_breakdown().items()))

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, new_limit):
        if not isinstance(new_limit, (int, float)):
            raise ValueError("Limit must be a number")
        if new_limit < 0:
            raise ValueError("Limit cannot be less than zero")
        self._limit = new_limit
        
    def detect_overspending(self, limit=None):
        if limit is None:
            limit = self.limit

        total_expenses = self.get_total_expenses()

        return total_expenses > limit

    def get_statistics(self):
        return {
            "total_income": self.get_total_income(),
            "total_expenses": self.get_total_expenses(),
            "balance": self.balance,
            "category_breakdown": self.get_category_breakdown(),
            "unique_categories": self.get_unique_categories(),
            "category_report_rows": self.get_category_report_rows()
        }

    def get_monthly_summary(self, month):
        month_transactions = list(filter(lambda transaction: transaction.date.startswith(month),self.transactions))
        total_income = sum(income.amount for income in month_transactions if isinstance(income, Income))
        total_expenses = sum(expense.amount for expense in month_transactions if isinstance(expense, Expense))

        return {
            "month": month,
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": total_income - total_expenses
        }
        
