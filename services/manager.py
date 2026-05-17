
class Manager:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

        
    def get_balance(self):
        return sum(i.sign_amount for i in self.transactions)
    