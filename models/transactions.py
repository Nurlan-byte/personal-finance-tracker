class Transaction:
    _id_counter = 1
    
    def __init__(self,  amount, date="14.05.2026"):
        self._amount = amount
        self.__id = Transaction._id_counter
        Transaction._id_counter += 1
        self._date = date
        
        
    @property
    def date(self):
        return self._date
        
    @property
    def amount(self):
        return self._amount
    
    def get_details(self):
        return {
            "id": self.__id,
            "amount": self._amount,
            "date": self._date
        }