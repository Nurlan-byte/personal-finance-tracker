class Manager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0

        for transaction in self.transactions:
            amount = transaction.get_amount()

            if transaction.__class__.__name__ == "Income":
                balance = balance + amount

            if transaction.__class__.__name__ == "Expense":
                balance = balance - amount

        return balance

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