def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            print("Exiting the calculator.")
            break

        if operation in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == '+':
                    print(f"Result: {add(num1, num2)}")
                elif operation == '-':
                    print(f"Result: {subtract(num1, num2)}")
                elif operation == '*':
                    print(f"Result: {multiply(num1, num2)}")
                elif operation == '/':
                    print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid operation! Please enter one of +, -, *, or /.")

if __name__ == "__main__":
    calculator()
