
from .transactions import Transaction

class Income(Transaction):
    
    def __init__(self, amount, date, source = "general"):
        super().__init__(amount, date)
        self.source = source
        
    def get_other(self):
        details = super().get_details()
        details["type"] = "income"
        details["source"] = self.source
        
        return details
    