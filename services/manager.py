class Manager:
    def __init__(self):
        self.transactions = []

    # Add new transaction
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    # Check if manager has transactions
    def has_transactions(self):
        if len(self.transactions) > 0:
            return True
        else:
            return False

    # Get only expense transactions
    def get_expenses(self):
        expenses = []

        for transaction in self.transactions:
            if transaction.__class__.__name__ == "Expense":
                expenses.append(transaction)

        return expenses

    # Get only income transactions
    def get_incomes(self):
        incomes = []

        for transaction in self.transactions:
            if transaction.__class__.__name__ == "Income":
                incomes.append(transaction)

        return incomes

    # Calculate balance
    def get_balance(self):
        balance = 0

        for income in self.get_incomes():
            balance = balance + income.get_amount()

        for expense in self.get_expenses():
            balance = balance - expense.get_amount()

        return balance

    # Group expenses by category
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

    # Calculate all expenses
    def get_total_expenses(self):
        total = 0

        for expense in self.get_expenses():
            total = total + expense.get_amount()

        return total

    # Calculate all incomes
    def get_total_income(self):
        total = 0

        for income in self.get_incomes():
            total = total + income.get_amount()

        return total

    # Check if expenses are higher than limit
    def detect_overspending(self, limit):
        total_expenses = self.get_total_expenses()

        if total_expenses > limit:
            print("Warning: overspending detected")
            return True
        else:
            print("No overspending")
            return False

    # Return all finance information
    def get_statistics(self):
        return {
            "total_income": self.get_total_income(),
            "total_expenses": self.get_total_expenses(),
            "balance": self.get_balance(),
            "category_breakdown": self.get_category_breakdown()
        }