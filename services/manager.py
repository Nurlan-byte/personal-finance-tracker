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