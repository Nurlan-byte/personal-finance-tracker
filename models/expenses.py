
from .transactions import Transaction

class Expense(Transaction):
    
    def __init__(self, amount, date, category):
        super().__init__(amount, date)
        self.category = category
        
    def get_details(self):
        details = super().get_details()
        details["type"] = "expense"
        details["category"] = self.category
        
        return details