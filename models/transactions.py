class Transaction:
    _id_counter = 1
    
    def __init__(self,  amount, date="14.05.2026"):
        self.__amount = amount
        self.__id = Transaction._id_counter
        self.date = date
        
        
    def set_date(self, date):
        self.date = date
    
    def get_date(self):
        return self.date
    
    def set_amount(self, amount):
        self.amount = amount
    
    def get_amount(self):
        return self.amount
    
    def get_other(self):
        pass