import json
import os

DATA_FILE = os.path.join("data", "transactions.json")

def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_transactions(transactions_list):
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(transactions_list, file, indent=4, ensure_ascii=False)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    test_data = [
        {"type": "expense", "category": "food", "amount": 20, "date": "2026-05-01"},
        {"type": "income", "amount": 1000, "date": "2026-05-01"}
    ]
    print("Saving test data with dates...")
    print(f"Save result: {save_transactions(test_data)}")
    print("\nLoading data back...")
    print(f"Loaded data: {load_transactions()}")