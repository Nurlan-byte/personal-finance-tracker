
from .transactions import Transaction

class Income(Transaction):
    
    def __init__(self, amount, date, source = "general"):
        super().__init__(amount, date)
        self._source = source
        
    @property
    def source(self):
        return self._source    
        
    def get_details(self):
        details = super().get_details()
        details["type"] = "income"
        details["source"] = self._source
        
        return details
    
    def sign_amount(self):
        return self._amount
    