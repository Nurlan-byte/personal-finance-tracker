from models.incomes import Income
from models.expenses import Expense


class Manager:
    def __init__(self):
        self._balance = 0
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self._balance += transaction.sign_amount()
        
    @property
    def balance(self):
        return self._balance
    