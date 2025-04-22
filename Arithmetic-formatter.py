def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top = []
    bottom = []
    lines = []
    results = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid format."

        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operators must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        top.append(num1.rjust(width))
        bottom.append(operator + " " + num2.rjust(width - 2))
        lines.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(width))

    arranged_problems = "    ".join(top) + "\n" + "    ".join(bottom) + "\n" + "    ".join(lines)
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')
