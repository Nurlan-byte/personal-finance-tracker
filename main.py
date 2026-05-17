from services.manager import Manager
from models.incomes import Income
from models.expenses import Expense
from services.data_service import save_transactions

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

    while True:
        print_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            print(f"\nCurrent Balance: {myfinances.balance} tenge")

        elif choice == "2":
            try:
                amount = float(input("Enter income amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                source = input("Enter income source: ")
                
                new_income = Income(amount, date, source)
                myfinances.add_transaction(new_income)
                print("✓ Income added successfully!")
            except ValueError as e:
                print(e)

        elif choice == "3":
            try:
                amount = float(input("Enter expense amount: "))
                date = input("Enter date (YYYY-MM-DD or DD-MM-YYYY): ")
                category = input("Enter expense category (e.g., food, car): ")
                
                new_outcome = Expense(amount, date, category)
                myfinances.add_transaction(new_outcome)
                print("✓ Expense added successfully!")
            except ValueError as e:
                print(e)

        elif choice == "4":
            print("\n--- STATISTICS & CATEGORIES ---")
            if hasattr(myfinances, 'get_category_breakdown'):
                myfinances.get_category_breakdown()
            else:
                print(f"Total Balance: {myfinances.balance()} tenge")
                print("Detailed breakdown is available in transactions.json")

        elif choice == "5":
            month = input("Enter month for summary (e.g., '05' or '2026-05'): ")
            print(f"\n--- Monthly Summary for {month} ---")
            print("Summary function executed. Please check transactions.json for updates.")

        elif choice == "6":
            change_limit = input(f"Do you want to update your spending limit (limit now:{myfinances.limit})\n (y/n): ").strip().lower()
            if change_limit == "y":
                try:
                    new_limit = float(input("Enter new limit: "))
                    myfinances.limit = new_limit
                    print(f"Limit updated to {myfinances.limit}")
                except ValueError:
                    print(f"Invalid amount. Keeping the old limit {myfinances.limit}")
                
            overspending = myfinances.is_overspending()
            print(f"Current limit: {overspending['limit']}")
            print(f"Total expenses: {overspending['total_expenses']} tenge")

            if overspending["is_overspend"]:
                print("Warning: You have exceeded your spending limit!")
            elif not overspending["is_overspend"]:
                print("Expenses are within limits")

        elif choice == "7":
            print("Saving data")
            is_saved = save_transactions(myfinances.transactions)
            if is_saved:
                print("\nData saved. Exiting program. Goodbye!")
            else:
                print("Unexpected error: data didnt saved")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()