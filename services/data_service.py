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
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(transactions_list, file, indent=4, ensure_ascii=False)
        return True
    except Exception:
        return False