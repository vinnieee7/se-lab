# A S Vincent SRN : PES2UG24CS002
"""
Library Fine and Book Renewal System.
Author: A S Vincent (SRN: PES2UG24CS002)

This module manages student book loans, overdue fine computations,
book renewals, and persistence of loan records to JSON.
"""

import ast
import json
import operator
from datetime import datetime

# Global loan database and default fine rate
loans = {}
FINE_PER_DAY = 2

_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def _eval_expr(node, context):
    """Safely evaluate arithmetic AST expressions with context variables."""
    if isinstance(node, ast.Expression):
        return _eval_expr(node.body, context)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in context:
            return context[node.id]
        raise ValueError(f"Undefined variable in rule: {node.id}")
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type in _ALLOWED_OPERATORS:
            left_val = _eval_expr(node.left, context)
            right_val = _eval_expr(node.right, context)
            return _ALLOWED_OPERATORS[op_type](left_val, right_val)
        raise ValueError(f"Operator not permitted: {op_type}")
    raise ValueError(f"Unsupported syntax: {type(node).__name__}")


def add_book_loan(student_id, book_id, dates=None):
    """Record a book loan for a student."""
    if not student_id:
        print("Error: Student ID cannot be empty.")
        return
    book_id_str = str(book_id)
    loan_dates = list(dates) if dates is not None else []
    loan_dates.append(str(datetime.now()))
    loans[student_id] = loans.get(student_id, []) + [book_id_str]
    msg = (
        f"{student_id} borrowed {book_id_str} "
        f"(loan dates on record: {len(loan_dates)})"
    )
    print(msg)


def return_book(student_id, book_id):
    """Return a borrowed book and update the loan records."""
    book_id_str = str(book_id)
    try:
        loans[student_id].remove(book_id_str)
        if len(loans[student_id]) == 0:
            del loans[student_id]
    except (KeyError, ValueError) as exc:
        print(f"Cannot return book {book_id_str} for {student_id}: {exc}")


def calculate_fine(days_overdue):
    """Calculate the fine for overdue days. Negative days incur no fine."""
    if days_overdue <= 0:
        return 0
    return days_overdue * FINE_PER_DAY


def renew_book(student_id, book_id, extra_days):
    """Renew a book for additional days."""
    book_id_str = str(book_id)
    if extra_days > 14:
        print(
            f"Notice: Extended renewal for {book_id_str} "
            f"({extra_days} days)."
        )
    print(f"Renewed {book_id_str} for {student_id} by {extra_days} days")


def load_records(file="loans.json"):
    """Load loan records from a JSON file into memory."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
            loans.clear()
            loans.update(data)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Error loading records from {file}: {exc}")


def save_records(file="loans.json"):
    """Save current loan records to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(loans, indent=2))


def fine_from_rule(rule, days):
    """Compute fine amount based on a custom rule string safely."""
    parsed = ast.parse(rule, mode="eval")
    return _eval_expr(parsed, {"days": days})


def print_report():
    """Display a summary of all active student loans."""
    print("Loan Report")
    for student, book_list in loans.items():
        print(f"{student} -> {book_list}")


def main():
    """Demonstrate library system operations."""
    add_book_loan("S101", "B-ALGO")
    add_book_loan("S102", "B-NETW")
    add_book_loan("", "B-DBMS")
    add_book_loan("S103", 4521)  # book id converted to string
    return_book("S999", "B-NONE")
    renew_book("S101", "B-ALGO", 21)
    print("Fine for 5 days:", calculate_fine(5))
    print("Fine for -3 days:", calculate_fine(-3))
    print("Fine via rule:", fine_from_rule("days * 2 + 10", 4))
    user_input = input("Days overdue for S102 (press Enter for 0): ") or "0"
    try:
        days = int(user_input)
    except ValueError:
        print("Invalid input, defaulting to 0 days overdue.")
        days = 0
    print("S102 owes:", calculate_fine(days))
    save_records()
    load_records()
    print_report()


if __name__ == "__main__":
    main()
