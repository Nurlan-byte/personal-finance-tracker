
from transactions import Transaction

class Expense(Transaction):
    
    def __init__(self, category):
        super().__init__(amount, date)
        self.category = category
        
    def get_other(self):
        return super().get_other()