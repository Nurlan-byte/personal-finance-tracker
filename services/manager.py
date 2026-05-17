from services import data_service
from models.expenses import Expense
from models.incomes import Income

class Manager:
    def __init__(self):
        self.transactions = []
        self._limit = 50000
        
        data = data_service.load_transactions()
        for transaction in data:
            if transaction["type"] == "income":
                new_income = Income(transaction["amount"], transaction["date"], transaction.get("source", "general"))
                self.transactions.append(new_income)
            if transaction["type"] == "expense":
                new_expense = Expense(transaction["amount"], transaction["date"], transaction.get("category", "general"))
                self.transactions.append(new_expense)
                
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def is_overspending(self):
        total_expenses =sum(abs(i.amount) for i in self.transactions if i.get_details().get("type") == "expense")
        return {
            "limit": self.limit,
            "total_expenses": total_expenses,
            "is_overspend": total_expenses > self.limit
        }

    @property
    def balance(self):
        return sum(i.sign_amount() for i in self.transactions)
    
    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self, new_limit):
        if new_limit < 0:
            raise ValueError("Limit cannot be less than zero")
        self._limit = new_limit

    