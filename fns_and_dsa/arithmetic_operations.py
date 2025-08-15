def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = str(input("Enter the operation ('add', 'subtract', 'multiply', or 'divide'): ")).strip().lower()
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2 
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    return f"The result of {operation}ing {num1} and {num2} is: {result}"
print(perform_operation())