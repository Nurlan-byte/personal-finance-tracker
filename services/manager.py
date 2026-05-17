class Manager:
    def __init__(self, limit=50000):
        self.transactions = []
        self.limit = limit

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_type(self, transaction):
        return transaction.get_details().get("type")

    def get_amount(self, transaction):
        return transaction.amount

    def get_expenses(self):
        return list(filter(
            lambda transaction: self.get_type(transaction) == "expense",
            self.transactions
        ))

    def get_incomes(self):
        return list(filter(
            lambda transaction: self.get_type(transaction) == "income",
            self.transactions
        ))

    def get_total_expenses(self):
        amounts = map(lambda expense: self.get_amount(expense), self.get_expenses())
        return sum(amounts)

    def get_total_income(self):
        amounts = map(lambda income: self.get_amount(income), self.get_incomes())
        return sum(amounts)

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    def get_category_breakdown(self):
        result = {}

        for expense in self.get_expenses():
            category = expense.category
            amount = self.get_amount(expense)

            if category in result:
                result[category] += amount
            else:
                result[category] = amount

        return result

    def detect_overspending(self, limit=None):
        if limit is None:
            limit = self.limit

        total_expenses = self.get_total_expenses()

        if total_expenses > limit:
            print("Warning: overspending detected")
            return True

        print("No overspending")
        return False

    def get_statistics(self):
        return {
            "total_income": self.get_total_income(),
            "total_expenses": self.get_total_expenses(),
            "balance": self.get_balance(),
            "category_breakdown": self.get_category_breakdown()
        }

    def get_monthly_summary(self, month):
        month_transactions = list(filter(
            lambda transaction: transaction.date.startswith(month),
            self.transactions
        ))

        month_income = list(filter(
            lambda transaction: self.get_type(transaction) == "income",
            month_transactions
        ))

        month_expenses = list(filter(
            lambda transaction: self.get_type(transaction) == "expense",
            month_transactions
        ))

        total_income = sum(map(lambda income: income.amount, month_income))
        total_expenses = sum(map(lambda expense: expense.amount, month_expenses))

        return {
            "month": month,
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": total_income - total_expenses
        }