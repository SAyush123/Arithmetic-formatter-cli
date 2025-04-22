#  Arithmetic Arranger

A Python function that takes a list of arithmetic problems and returns them arranged vertically and side-by-side, just like how you'd see in a school notebook.

###  Features
- Accepts up to 5 arithmetic problems.
- Supports only addition and subtraction (`+` and `-`).
- Validates input for:
  - Too many problems.
  - Invalid operators.
  - Non-digit characters.
  - Numbers exceeding four digits.
- Optionally displays the result of each operation.
- Neatly formats the output.

---

###  Function Signature

```python
arithmetic_arranger(problems: list, show_answers: bool = False) -> str
