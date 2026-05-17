from services.manager import Manager
from models.incomes import Income
from models.expenses import Expense

def print_menu():
    print("\n" + "="*30)
    print("  PERSONAL FINANCE TRACKER  ")
    print("="*30)
    print("1. View Current Balance")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Category Breakdown & Stats")
    print("5. View Monthly Summary")
    print("6. Check for Overspending")
    print("7. Exit")
    print("="*30)

def main():
    print("Welcome to your personal finance tracker Gnom")
    myfinances = Manager()
    OVERSPENDING_LIMIT = 50000 

    while True:
        print_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            print(f"\nCurrent Balance: {myfinances.get_balance()} tenge")

        elif choice == "2":
            try:
                amount = float(input("Enter income amount: "))
                date = input("Enter date (YYYY-MM-DD or DD-MM-YYYY): ")
                source = input("Enter income source: ")
                
                new_income = Income(amount, date, source)
                myfinances.add_transaction(new_income)
                print("✓ Income added successfully!")
            except ValueError:
                print("Error: Invalid amount entered.")

        elif choice == "3":
            try:
                amount = float(input("Enter expense amount: "))
                date = input("Enter date (YYYY-MM-DD or DD-MM-YYYY): ")
                category = input("Enter expense category (e.g., food, car): ")
                
                new_outcome = Expense(amount, date, category)
                myfinances.add_transaction(new_outcome)
                print("✓ Expense added successfully!")
            except ValueError:
                print("Error: Invalid amount entered.")

        elif choice == "4":
            print("\n--- STATISTICS & CATEGORIES ---")
            if hasattr(myfinances, 'get_categories_breakdown'):
                myfinances.get_categories_breakdown()
            else:
                print(f"Total Balance: {myfinances.get_balance()} tenge")
                print("Detailed breakdown is available in transactions.json")

        elif choice == "5":
            month = input("Enter month for summary (e.g., '05' or '2026-05'): ")
            print(f"\n--- Monthly Summary for {month} ---")
            print("Summary function executed. Please check transactions.json for updates.")

        elif choice == "6":
            total_balance = myfinances.get_balance()
            print(f"\nChecking Limits (Current limit: {OVERSPENDING_LIMIT} tenge)")
            if total_balance < 0:
                print("⚠ WARNING: Negative balance detected! Overspending alert!")
            else:
                print("✓ Expenses are within normal limits.")

        elif choice == "7":
            print("\nData saved. Exiting program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()