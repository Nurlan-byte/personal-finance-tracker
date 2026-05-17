from models.incomes import Income
from models.expenses import Expense

class Manager:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    def get_balance(self):
        sum = 0
        for i in self.transactions:
            if isinstance(i, Income):
                sum += i._amount
            elif isinstance(i, Expense):
                sum -= i._amount
        return sum
    