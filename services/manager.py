class Manager:
    def __init__(self, limit=50000):
        self.transactions = []
        self._limit = limit

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, new_limit):
        self._limit = new_limit

    def get_amount(self, transaction):
        return transaction.amount

    def get_type(self, transaction):
        return transaction.get_details().get("type")

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
        expenses = self.get_expenses()
        amounts = map(lambda expense: self.get_amount(expense), expenses)
        return sum(amounts)

    def get_total_income(self):
        incomes = self.get_incomes()
        amounts = map(lambda income: self.get_amount(income), incomes)
        return sum(amounts)

    def get_balance(self):
        return self.get_total_income() - self.get_total_expenses()

    @property
    def balance(self):
        return self.get_balance()

    def get_category_breakdown(self):
        result = {}

        for expense in self.get_expenses():
            category = expense.category
            amount = self.get_amount(expense)

            if category in result:
                result[category] = result[category] + amount
            else:
                result[category] = amount

        return result

    def detect_overspending(self, limit):
        total_expenses = self.get_total_expenses()

        if total_expenses > limit:
            print("Warning: overspending detected")
            return True
        else:
            print("No overspending")
            return False

    def is_overspending(self):
        total_expenses = self.get_total_expenses()

        return {
            "limit": self.limit,
            "total_expenses": total_expenses,
            "is_overspend": total_expenses > self.limit
        }

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

        income_transactions = list(filter(
            lambda transaction: self.get_type(transaction) == "income",
            month_transactions
        ))

        expense_transactions = list(filter(
            lambda transaction: self.get_type(transaction) == "expense",
            month_transactions
        ))

        total_income = sum(map(lambda income: income.amount, income_transactions))
        total_expenses = sum(map(lambda expense: expense.amount, expense_transactions))

        return {
            "month": month,
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": total_income - total_expenses
        }