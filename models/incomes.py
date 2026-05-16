
from transactions import Transaction

class Income(Transaction):
    
    def __init__(self, amount, date, inc_category = "general"):
        super().__init__(amount, date)
        self.inc_category = inc_category
        
    def get_other(self):
        return super().get_other()
    