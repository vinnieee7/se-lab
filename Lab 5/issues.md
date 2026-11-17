# Static Code Analysis Issue Documentation

This document records the quality, style, and security issues identified in `library_system.py` using **Pylint**, **Bandit**, and **Flake8**, prioritized by severity.

## Summary of Initial Analysis Results

- **Pylint Score (Initial):** 6.07 / 10
- **Bandit Findings (Initial):** 2 issues (1 Medium severity CWE-78, 1 Low severity CWE-703)
- **Flake8 Violations (Initial):** 14 violations (F401, E722, E501, E302, E305)

---

## Issue Documentation Table

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Arbitrary Code Execution via `eval()` (Bandit B307 / CWE-78 / Pylint W0123) | Security (High) | 45 | `fine_from_rule()` used Python's built-in `eval()` on raw input strings. An untrusted input rule can execute arbitrary Python commands and system calls (e.g. `__import__("os").system(...)`), compromising the host system. | Replaced `eval()` with a secure Abstract Syntax Tree (`ast`) evaluator using `ast.parse(rule, mode="eval")` that strictly validates nodes against a whitelist of safe arithmetic operations (`+`, `-`, `*`, `/`) and allowed variables (`days`), preventing arbitrary execution. |
| Dangerous Mutable Default Argument (Pylint W0102 / Logic Bug) | Logic & Quality (High) | 9 | `add_book_loan()` defined `dates=[]` as a default argument. In Python, mutable default arguments are instantiated once at function definition and shared across all calls. Consequently, loan dates accumulated globally across different student calls. | Replaced default parameter with `dates=None` and initialized `loan_dates = list(dates) if dates is not None else []` inside the function scope to ensure independent lists per invocation. |
| Bare Except and Pass (Bandit B110 / CWE-703 / Pylint W0702 / Flake8 E722) | Security & Robustness (Medium) | 21-22 | `return_book()` wrapped dictionary removal in a bare `except: pass` block. This masked all exceptions indiscriminately (including `KeyError`, `ValueError`, and critical signals like `KeyboardInterrupt`), silently failing without notifying the user or administrator. | Replaced bare `except:` with explicit exception handling for expected failure modes (`except (KeyError, ValueError) as exc:`) and added meaningful error logging instead of silently ignoring failures. |
| Global State Mutation and Permanent Rate Inflation (Pylint W0603 / Logic Bug) | Architecture & Logic (Medium) | 28-30, 35 | `renewBook()` used `global FINE_PER_DAY` to increment the daily fine rate whenever any single book was renewed for >14 days. This permanently increased the fine rate for all other students and future calculations. `load_records()` also relied on `global loans`. | Removed global mutation of `FINE_PER_DAY` to preserve the constant rate invariant. Refactored `load_records()` to update the `loans` dictionary in-place (`loans.clear()`, `loans.update(data)`) without rebinding the global variable. |
| Unmanaged File Resources and Missing Encoding (Pylint R1732, W1514) | Resource Management (Medium) | 34, 40 | `load_records()` and `save_records()` used unmanaged `open()` calls without context managers or explicit UTF-8 encoding. If an error occurred prior to `f.close()`, file descriptors would leak, and encoding defaults could cause platform inconsistencies. | Refactored file operations to use `with open(file, mode, encoding="utf-8") as f:` blocks, guaranteeing deterministic resource cleanup and portable UTF-8 encoding. |
| Unused Import `os` (Flake8 F401 / Pylint W0611) | Code Hygiene (Low) | 2 | `import os` was declared at the top of the module but never referenced anywhere in the script, polluting the module namespace. | Removed the unused `import os` statement. |
| PEP 8 Style, Blank Lines & Line Lengths (Flake8 E302, E305, E501) | Style & Readability (Low) | 9, 14, 16, 24, 27, 31, 33, 39, 44, 47, 52, 68 | Multiple PEP 8 style violations: missing 2 blank lines between top-level functions, single blank line after function definition, and print statements exceeding the standard 79-character maximum limit. | Reformatted spacing to ensure 2 blank lines between all top-level definitions, wrapped long statements across lines, and replaced `%`-formatting with readable f-strings. |
| Missing Docstrings & Non-Standard Function Naming (Pylint C0114, C0116, C0103) | Maintainability (Low) | 1, 9, 16, 24, 27, 33, 39, 44, 47, 52 | The module and its functions lacked documentation explaining purpose, inputs, and outputs. Function name `renewBook` violated PEP 8 `snake_case` naming conventions. | Added comprehensive module and function docstrings; renamed `renewBook` to `renew_book` conforming to snake_case naming standards. |
