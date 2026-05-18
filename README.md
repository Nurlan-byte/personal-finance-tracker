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

The project demonstrates:

- clean Python module structure;
- object-oriented programming;
- file handling with JSON;
- input validation and exception handling;
- practical use of collections;
- basic algorithmic efficiency;
- unit testing with `unittest`.

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

## How To Run Tests

```bash
python -m unittest tests.test
```

Current expected result:

```text
Ran 10 tests
OK
```

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

## Module Responsibilities

| File | Responsibility |
| --- | --- |
| `main.py` | Runs the command-line menu and handles user interaction. |
| `models/transactions.py` | Contains the base `Transaction` class. |
| `models/incomes.py` | Contains the `Income` class. |
| `models/expenses.py` | Contains the `Expense` class. |
| `services/manager.py` | Contains the main finance logic and calculations. |
| `services/data_service.py` | Loads and saves transactions using JSON. |
| `utils/helpers.py` | Validates dates and amounts. |
| `tests/test.py` | Contains automated unit tests. |

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

The project uses four main classes:

| Class | Purpose |
| --- | --- |
| `Transaction` | Base class for all financial transactions. |
| `Income` | Child class for money received by the user. |
| `Expense` | Child class for money spent by the user. |
| `Manager` | Service class that stores transactions and calculates reports. |

### Encapsulation

Transaction data is stored in protected/private fields:

- `_amount`
- `_date`
- `_source`
- `_category`
- `__id`

The program uses properties such as `amount`, `date`, `source`, `category`, and
`limit` to control access to important values.

### Inheritance

`Income` and `Expense` both inherit from `Transaction`.

This avoids duplicating shared fields such as:

- amount;
- date;
- transaction id.

### Polymorphism

Both `Income` and `Expense` implement `sign_amount()`, but they behave differently:

```python
Income.sign_amount()   # returns a positive amount
Expense.sign_amount()  # returns a negative amount
```

Because of this, the balance can be calculated with one simple expression:

```python
sum(t.sign_amount() for t in self.transactions)
```

## Requirement Coverage

| Requirement | How It Is Covered |
| --- | --- |
| Functions | Functions and methods are used across all modules. |
| Arguments and return values | Methods such as `get_monthly_summary(month)` return dictionaries with calculated data. |
| Control flow | The menu uses conditions and loops; calculations use loops and filtering. |
| Error handling | Invalid dates, negative amounts, bad limits, and broken JSON are handled. |
| OOP | `Transaction`, `Income`, `Expense`, and `Manager` are used. |
| Encapsulation | Protected/private fields and properties are used. |
| Inheritance | `Income` and `Expense` inherit from `Transaction`. |
| Polymorphism | `sign_amount()` behaves differently for income and expense. |
| Lists | `Manager.transactions` stores all transaction objects. |
| Dictionaries | Category breakdown and monthly summary use dictionaries. |
| Tuples | `get_category_report_rows()` returns fixed report rows as tuples. |
| Sets | `get_unique_categories()` returns unique categories as a set. |
| File handling | Transactions are loaded from and saved to JSON. |
| Modules | Code is split into `models`, `services`, `utils`, and `tests`. |
| Testing | `tests/test.py` uses `unittest`. |
| Advanced Python | Uses properties, lambdas, `map`, `filter`, and generator expressions. |

## Collections And Data Structures

The project uses several data structures for clear reasons.

### List

`Manager.transactions` is a list because transactions must be stored together and
processed in order.

```python
self.transactions = []
```

### Dictionary

Category breakdown uses a dictionary:

```python
{
    "food": 23500,
    "rent": 80000,
    "transport": 6500
}
```

This is efficient because each category can be updated directly by key.

### Set

Unique categories are stored in a set:

```python
{"food", "rent", "transport"}
```

A set is the right structure here because it automatically removes duplicates.

### Tuple

Category report rows are returned as a tuple:

```python
(("food", 23500), ("rent", 80000))
```

A tuple is suitable because each row is a fixed pair: `(category, total_amount)`.

## Algorithmic Efficiency

The most important efficiency decision is the use of a dictionary in
`get_category_breakdown()`.

Current approach:

```python
if category in result:
    result[category] += amount
else:
    result[category] = amount
```

Why this is efficient:

- A dictionary gives direct access to a category total by category name.
- Updating a category is usually `O(1)`.
- Processing all expenses is close to `O(n)`, where `n` is the number of expenses.

A less efficient approach would store category totals in a list and search through
that list for every expense. That can become close to `O(n * k)`, where `k` is the
number of categories.

Other efficiency choices:

- `sum()` is used for total calculations.
- `filter()` separates income and expenses clearly.
- `map()` extracts amounts before summing.
- A generator expression calculates balance without building an extra list.
- A set comprehension collects unique categories in one pass.

## Advanced Python Features

The project uses these advanced Python features:

- `@property` decorators for controlled field access;
- lambda functions in `filter()` and `map()`;
- generator expression in the `balance` property;
- set comprehension in `get_unique_categories()`;
- tuple conversion in `get_category_report_rows()`;
- exception handling with `try` / `except`.

## Validation And Error Handling

The application validates important input:

- amount must be numeric;
- amount cannot be negative;
- date must use `YYYY-MM-DD`;
- spending limit must be a non-negative number;
- missing JSON file returns an empty list;
- invalid JSON returns an empty list;
- invalid transaction records are skipped during loading.

This prevents the program from crashing during common user or file errors.

## Testing

The test suite is written with `unittest`.

Tests cover:

- empty manager state;
- adding income;
- adding expenses;
- balance calculation;
- category breakdown;
- unique category set;
- tuple-based category report rows;
- overspending detection;
- monthly summary;
- real `Income` and `Expense` objects;
- negative amount validation;
- invalid date validation;
- zero-amount transaction;
- JSON save and load behavior.

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
| **Yussupov Nurlan** | System architecture, OOP design (Models, Encapsulation, Polymorphism), and integrating all modules together. |
| **Asylzhan Amangeldi** | Advanced analytical functions (`lambda`, `map`, `filter`), category breakdowns, monthly summary logic. |
| **Dias Sabit** | File handling (`data_service.py`), JSON serialization/deserialization, and data persistence logic. |
| **Bakdaulet Begaliev** | Command-line interface (Menu in `main.py`), user interaction, and automated unit testing (`tests/test.py`). |
