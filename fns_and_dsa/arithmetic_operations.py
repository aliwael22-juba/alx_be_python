def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation ('add', 'subtract', 'multiply', 'divide'): ").strip().lower()  
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2 
    elif operation == 'divide':
        if num2 == 0:
              print("Error: Division by zero is not allowed.")
              return
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operation.") 
    print(f"The result of {operation}ing {num1} and {num2} is: {result}") 

perform_operation("num1","num2","operation")