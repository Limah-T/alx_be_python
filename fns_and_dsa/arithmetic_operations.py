def perform_operation(num1, num2, operation):
    if operation == 'add':
        num1 + num2
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == 'subtract':
        num1 - num2
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == 'multiply':
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == 'divide':
        if num2 == 0:
            print(f"{num1} cannot be divided by 0")
        else:
            result = num1 / num2
            print(f"Result: {result}")