import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from services.manager import Manager

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


if __name__ == "__main__":
    unittest.main()