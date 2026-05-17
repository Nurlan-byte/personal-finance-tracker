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
            breakdown = myfinances.get_category_breakdown()
            if not breakdown:
                print("No expenses found.")
            else:
                for cat, amount in breakdown.items():
                    print(f"- {cat.capitalize()}: {amount} tenge")

        elif choice == "5":
            month = input("Enter month for summary (e.g., '2026-05'): ").strip()
            if not month:
                print("Error: Month cannot be empty!")
                continue
            summary = myfinances.get_monthly_summary(month) 
            print(f"\n--- Monthly Summary for {summary['month']} ---")
            print(f"Total Income:   {summary['total_income']} tenge")
            print(f"Total Expenses: {summary['total_expenses']} tenge")
            print(f"Month Balance:  {summary['balance']} tenge")

        elif choice == "6":
            print(f"\n--- OVERSPENDING CHECK ---")
            print(f"Current expense limit: {myfinances.limit} tenge")
            if myfinances.detect_overspending():
                print("⚠ WARNING: Overspending detected! You exceeded your limit!")
            elif myfinances.balance < 0:
                print("⚠ WARNING: Negative total balance detected!")
            else:
                print("✓ Expenses are within normal limits.")
                
            change = input("\nDo you want to change the limit? (y/n): ").strip().lower()
            if change == 'y':
                try:
                    new_limit = float(input("Enter new overspending limit: "))
                    myfinances.limit = new_limit
                    print(f"✓ Limit successfully updated to {myfinances.limit} tenge!")
                except ValueError as e:
                    print(f"Error: {e}")

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