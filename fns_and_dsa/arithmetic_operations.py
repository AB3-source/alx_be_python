def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def perform_operation(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Please choose +, -, *, or /.")