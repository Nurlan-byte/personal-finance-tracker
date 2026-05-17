import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import tempfile
import json
from services.manager import Manager
from models.incomes import Income
from models.expenses import Expense
from services import data_service

class MockTransaction:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

class MockIncome(MockTransaction):
    def sign_amount(self):
        return self.amount

    def get_details(self):
        return {"type": "income"}

class MockExpense(MockTransaction):
    def __init__(self, amount, date, category):
        super().__init__(amount, date)
        self.category = category

    def sign_amount(self):
        return -self.amount

    def get_details(self):
        return {"type": "expense"}


class TestFinanceTracker(unittest.TestCase):

    def setUp(self):
        self.manager = Manager()
        self.manager.transactions = []
        self.manager.limit = 10000

    def test_initial_state(self):
        self.assertEqual(self.manager.balance, 0)
        self.assertEqual(self.manager.get_category_breakdown(), {})

    def test_add_income(self):
        income = MockIncome(50000, "2026-05-17")
        self.manager.add_transaction(income)
        self.assertEqual(self.manager.balance, 50000)

    def test_add_expense_and_breakdown(self):
        expenses = [
            MockExpense(3000, "2026-05-17", "food"),
            MockExpense(2000, "2026-05-18", "food"),
            MockExpense(1500, "2026-05-19", "car")
        ]
        for exp in expenses:
            self.manager.add_transaction(exp)
        
        breakdown = self.manager.get_category_breakdown()
        self.assertEqual(breakdown.get("food"), 5000)
        self.assertEqual(breakdown.get("car"), 1500)
        self.assertEqual(self.manager.get_unique_categories(), {"food", "car"})
        self.assertEqual(
            self.manager.get_category_report_rows(),
            (("car", 1500), ("food", 5000))
        )

    def test_overspending_detection(self):
        self.manager.add_transaction(MockExpense(8000, "2026-05-17", "rent"))
        self.assertFalse(self.manager.detect_overspending())

        self.manager.add_transaction(MockExpense(3000, "2026-05-18", "food"))
        self.assertTrue(self.manager.detect_overspending())

    def test_monthly_summary(self):
        self.manager.add_transaction(MockIncome(10000, "2026-05-01"))
        self.manager.add_transaction(MockExpense(2000, "2026-05-15", "food"))
        self.manager.add_transaction(MockExpense(4000, "2026-06-01", "other"))

        summary_may = self.manager.get_monthly_summary("2026-05")
        self.assertEqual(summary_may["total_income"], 10000)
        self.assertEqual(summary_may["total_expenses"], 2000)
        self.assertEqual(summary_may["balance"], 8000)

    def test_real_income_and_expense(self):
        income = Income(2000, "2026-05-10")
        expense = Expense(500, "2026-05-11", "transport")

        self.manager.add_transaction(income)
        self.manager.add_transaction(expense)

        self.assertEqual(self.manager.balance, 1500)

    def test_invalid_negative_income(self):
        with self.assertRaises(ValueError):
            Income(-1000, "2026-05-17")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Expense(1000, "invalid-date", "food")

    def test_zero_amount_transaction(self):
        income = Income(0, "2026-05-20")
        self.manager.add_transaction(income)

        self.assertEqual(self.manager.balance, 0)

    def test_save_and_load_json(self):
        original_data_file = data_service.DATA_FILE

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                data_service.DATA_FILE = os.path.join(temp_dir, "transactions.json")
                self.manager.add_transaction(Income(5000, "2026-05-17"))

                self.assertTrue(data_service.save_transactions(self.manager.transactions))

                with open(data_service.DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)

                self.assertEqual(data[0]["amount"], 5000)
                self.assertEqual(data[0]["type"], "income")

                new_manager = Manager()
                self.assertEqual(new_manager.balance, 5000)
        finally:
            data_service.DATA_FILE = original_data_file


if __name__ == "__main__":
    unittest.main()
