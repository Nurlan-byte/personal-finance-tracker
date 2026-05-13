class Transaction:
    _id_counter = 1
    
    def __init__(self,  amount, date="14.05.2026"):
        self.__amount = amount
        self.__id = Transaction._id_counter
        self.date = date
        
        
    def set_transaction(self):
        # TODO: setter 
        pass
    
    def get_transaction(self):
        pass
    
    def set_amount(self):
        pass
    
    def get_amount(self):
        pass