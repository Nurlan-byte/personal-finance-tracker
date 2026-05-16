from services.manager import Manager
from models.incomes import Income
from models.expenses import Expense

def main():
    print("Welcome to your personal finance tracker Gnom")
    myfinances = Manager()

    stipendia = Income(55000, "16-05-2026", "University")
    benzin = Expense(3000, "16-05-2026", "Car")
    
    myfinances.add_transaction(stipendia)
    myfinances.add_transaction(benzin)
    
    print(f"Balance: {myfinances.get_balance()} tenge")
if __name__ == "__main__":
    main()
    
    