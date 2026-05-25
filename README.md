# Personal Finance Tracker

Personal Finance Tracker is a command-line Python application for managing income
and expenses. The program helps users record transactions, calculate balance, group
expenses by category, generate monthly summaries, and detect overspending.

This project was built for the **Introduction to Programming 2 (Python)** final
project and implements **Case 3: Personal Finance Tracker**.

## Team Members

- Yussupov Nurlan
- Asylzhan Amangeldi
- Bakdaulet Begaliev
- Dias Sabit

## Project Goal

The goal of this project is to simulate a real personal finance tracking system.
Instead of storing information only while the program is running, the application
saves transaction data in a JSON file and loads it again when the program starts.

## Main Features

- Add income transactions with amount, date, and source.
- Add expense transactions with amount, date, and category.
- View current balance.
- View total income and total expenses.
- View category breakdown for expenses.
- View unique expense categories.
- Generate monthly summaries by `YYYY-MM`.
- Detect overspending using a configurable spending limit.
- Save transactions to `data/transactions.json`.
- Load saved transactions when the program starts.
- Run automated unit tests.

## How To Run

This project has no external library dependencies. Python standard library is
enough.

1. Clone the repository:

```bash
git clone <repository-url>
cd personal-finance-tracker
```

2. Run the program:

```bash
python main.py
```

3. Use the menu:

```text
1. View Current Balance
2. Add Income
3. Add Expense
4. View Category Breakdown & Stats
5. View Monthly Summary
6. Check for Overspending
7. Exit
```


## Example JSON Data

Transactions are stored in `data/transactions.json`.

```json
[
    {
        "id": 1,
        "amount": 250000.0,
        "date": "2026-05-01",
        "type": "income",
        "source": "salary"
    },
    {
        "id": 2,
        "amount": 80000.0,
        "date": "2026-05-02",
        "type": "expense",
        "category": "rent"
    }
]
```

## Example Output

Example category report:

```text
--- STATISTICS & CATEGORIES ---
Unique categories: 3
Categories: food, rent, transport
- Food: 23500 tenge
- Rent: 80000 tenge
- Transport: 6500 tenge
```

Example monthly summary:

```text
--- Monthly Summary for 2026-05 ---
Total Income:   265000 tenge
Total Expenses: 136500 tenge
Month Balance:  128500 tenge
```

## Team Contribution Breakdown

| Team Member | Main Contribution |
| --- | --- |
| **Yussupov Nurlan** | OOP design and integration of all modules together. |
| **Asylzhan Amangeldi** | Advanced analytical functions (`lambda`, `map`, `filter`), category breakdowns, monthly summary logic. |
| **Dias Sabit** | File handling (`data_service.py`), JSON serialization/deserialization, and data persistence logic. |
| **Bakdaulet Begaliev** | Command-line interface (Menu in `main.py`), user interaction, and automated unit testing (`tests/test.py`). |
