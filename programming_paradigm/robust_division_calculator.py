def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)

        if num2 == 0:
            return "Error: Cannot divide by zero."

        result = num1 / num2
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."