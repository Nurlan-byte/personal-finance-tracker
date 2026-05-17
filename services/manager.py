class Manager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_expenses(self):
        expenses = []

        for transaction in self.transactions:
            if transaction.__class__.__name__ == "Expense":
                expenses.append(transaction)

        return expenses

    def get_incomes(self):
        incomes = []

        for transaction in self.transactions:
            if transaction.__class__.__name__ == "Income":
                incomes.append(transaction)

        return incomes

    def get_balance(self):
        balance = 0

        for income in self.get_incomes():
            balance = balance + income.get_amount()

        for expense in self.get_expenses():
            balance = balance - expense.get_amount()

        return balance

    def get_category_breakdown(self):
        result = {}

        for expense in self.get_expenses():
            category = expense.category
            amount = expense.get_amount()

            if category in result:
                result[category] = result[category] + amount
            else:
                result[category] = amount

        return result

    def get_total_expenses(self):
        total = 0

        for expense in self.get_expenses():
            total = total + expense.get_amount()

        return total

    def get_total_income(self):
        total = 0

        for income in self.get_incomes():
            total = total + income.get_amount()

        return total

    def detect_overspending(self, limit):
        total_expenses = self.get_total_expenses()

        if total_expenses > limit:
            print("Warning: overspending detected")
            return True
        else:
            print("No overspending")
            return False