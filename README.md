# Personal Finance Tracker

A command-line Python application for tracking personal income and expenses, storing
transactions in JSON, calculating balances, generating monthly summaries, showing
category breakdowns, and detecting overspending.

This project was created for the **Introduction to Programming 2 (Python)** final
project. It implements **Case 3: Personal Finance Tracker**.

## Team Members

- Yussupov Nurlan
- Asylzhan Amangeldi
- Bakdaulet Begaliev
- Dias Sabit

## Problem Description

Many people record their spending manually or do not track it at all. This makes it
hard to understand where money goes each month and whether expenses are becoming too
high. The Personal Finance Tracker solves this by letting users:

- add income transactions;
- add expense transactions;
- group expenses by category;
- check the current balance;
- view monthly summaries;
- detect when total expenses exceed a chosen limit;
- save and load data automatically from a JSON file.

## Main Features

- **Current balance**: calculates total income minus total expenses.
- **Add income**: stores amount, date, and source.
- **Add expense**: stores amount, date, and category.
- **Category breakdown**: shows how much was spent in each expense category.
- **Monthly summary**: shows income, expenses, and balance for a selected month.
- **Overspending detection**: compares total expenses with a configurable limit.
- **JSON persistence**: saves transactions to `data/transactions.json`.
- **Input validation**: validates dates, amounts, and overspending limits.
- **Unit tests**: tests important finance calculations and edge cases.

## Project Structure

```text
personal-finance-tracker/
|-- data/
|   `-- transactions.json
|-- models/
|   |-- transactions.py
|   |-- incomes.py
|   `-- expenses.py
|-- services/
|   |-- data_service.py
|   `-- manager.py
|-- tests/
|   `-- test.py
|-- utils/
|   `-- helpers.py
|-- main.py
`-- README.md
```

## How To Run

1. Clone the repository:

```bash
git clone <repository-url>
cd personal-finance-tracker
```

2. Run the application:

```bash
python main.py
```

3. Choose an option from the menu:

```text
1. View Current Balance
2. Add Income
3. Add Expense
4. View Category Breakdown & Stats
5. View Monthly Summary
6. Check for Overspending
7. Exit
```

## How To Run Tests

Run the unit tests with:

```bash
python -m unittest tests.test
```

Expected result:

```text
Ran 5 tests
OK
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

## Object-Oriented Design

The project uses object-oriented programming to model financial transactions.

### `Transaction`

Base class for all transactions. It stores common fields:

- transaction id;
- amount;
- date.

It also provides shared methods such as `get_details()` and `sign_amount()`.

### `Income`

Derived from `Transaction`. It represents money received by the user.

- Adds a `source` field.
- Overrides `get_details()`.
- Overrides `sign_amount()` to return a positive amount.

### `Expense`

Derived from `Transaction`. It represents money spent by the user.

- Adds a `category` field.
- Overrides `get_details()`.
- Overrides `sign_amount()` to return a negative amount.

### `Manager`

Service class that controls the main finance logic:

- stores all transactions;
- calculates balance;
- separates income and expenses;
- generates category breakdowns;
- creates monthly summaries;
- detects overspending.

## OOP Concepts Used

- **Encapsulation**: transaction fields such as `_amount`, `_date`, `_source`, and
  `_category` are protected and accessed through properties.
- **Inheritance**: `Income` and `Expense` inherit from `Transaction`.
- **Polymorphism**: `Income` and `Expense` both implement `sign_amount()`, but each
  class returns the amount differently.

## Data Structures Used

- **List**: `Manager.transactions` stores all transaction objects in order.
- **Dictionary**: category breakdowns are stored as `{category: total_amount}` for
  fast lookup and updating.
- **List of dictionaries**: JSON data is loaded as a list of transaction records.
- **Set**: `get_unique_categories()` returns unique expense categories without
  duplicates, for example `{"food", "rent", "transport"}`.
- **Tuple**: `get_category_report_rows()` returns stable report rows as tuples,
  for example `(("food", 23000), ("rent", 80000))`.

Dictionary usage is especially important in `get_category_breakdown()`. Instead of
searching through all previous categories every time, the program updates totals by
key. This keeps category aggregation efficient and simple.

## Algorithms And Efficiency

The project avoids unnecessary nested loops in important calculations.

- Balance calculation uses `sum()` over transactions.
- Expense and income filtering uses `filter()` with lambda expressions.
- Category totals use a dictionary, making updates direct by category name.
- Unique categories use a set, because sets automatically remove duplicates.
- Category report rows use tuples, because each row is a fixed pair:
  `(category, total_amount)`.
- Monthly summary filters transactions by month and then sums income and expenses.

Example optimization:

```python
if category in result:
    result[category] += amount
else:
    result[category] = amount
```

Using a dictionary allows direct access to a category total by key. Without a
dictionary, the program would need to search through a list of existing categories
for every expense. That approach can become close to `O(n * k)`, where `n` is the
number of expenses and `k` is the number of categories. With a dictionary, each
category update is usually `O(1)`, so the whole category breakdown is closer to
`O(n)`.

## Advanced Python Features

The project uses several Python features beyond the basics:

- `@property` decorators for controlled access to fields;
- lambda functions in filtering and mapping operations;
- `map()` and `filter()` for income and expense calculations;
- generator expression in balance calculation:

```python
sum(t.sign_amount() for t in self.transactions)
```

## Error Handling And Validation

The project handles invalid input in several places:

- invalid amount values raise `ValueError`;
- negative amounts are rejected;
- invalid dates are rejected;
- invalid overspending limits are rejected;
- broken or missing JSON files return an empty transaction list instead of crashing;
- invalid transaction records are skipped during loading.

## File Handling

The project reads and writes structured JSON data:

- `load_transactions()` reads transaction data from `data/transactions.json`;
- `save_transactions()` writes current transaction data back to JSON;
- `os.makedirs()` creates the `data/` folder if it does not exist.

## Testing

The test file `tests/test.py` uses the `unittest` module. Current tests cover:

- initial empty manager state;
- adding income;
- adding expenses;
- category breakdown calculation;
- unique category set calculation;
- tuple-based category report rows;
- overspending detection;
- monthly summary calculation.

These tests help verify the correctness of the main finance logic.

## Team Contribution Breakdown

- **Yussupov Nurlan**: manager service logic, statistics, overspending detection,
  refactoring, and unit tests.
- **Asylzhan Amangeldi**: manager fixes, transaction loading improvements, finance
  calculations, and integration work.
- **Bakdaulet Begaliev**: transaction model support, data handling, and validation.
- **Dias Sabit**: command-line interface support, testing support, and project
  polishing.

## Code Defense Notes

During the code defense, each team member should be ready to explain:

- how `Transaction`, `Income`, and `Expense` demonstrate inheritance;
- why `sign_amount()` is polymorphic;
- how JSON loading and saving works;
- why dictionaries are useful for category breakdowns;
- how sets remove duplicate expense categories;
- why tuples are suitable for fixed report rows;
- how monthly summary filtering works;
- what edge cases are covered by tests;
- how invalid input is handled.

## Future Improvements

- Add editing and deleting existing transactions.
- Add a search feature by category, source, or date.
- Add CSV export for reports.
- Add charts for monthly spending.
- Add more tests for invalid input and JSON file handling.
