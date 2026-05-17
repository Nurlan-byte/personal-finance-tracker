from services import data_service
from models.expenses import Expense
from models.incomes import Income

class Manager:
    def __init__(self):
        self.transactions = []
        
        data = data_service.load_transactions()
        for transaction in data:
            if transaction["type"] == "income":
                new_income = Income(transaction["amount"], transaction["date"], transaction.get("source", "general"))
                self.transactions.append(new_income)
            if transaction["type"] == "expense":
                new_expense = Expense(transaction["amount"], transaction["date"], transaction.get("category", "general"))
                self.transactions.append(new_expense)
                
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    @property
    def balance(self):
        return sum(i.sign_amount() for i in self.transactions)
    