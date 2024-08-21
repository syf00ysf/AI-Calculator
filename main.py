# basic calculation functions
def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b
def calculator():
    operation = input("Enter the operation(add, substract, multiply, divide): ")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if operation == "add":
        print(addition(a,b))
    elif operation == "substract":
        print(substraction(a,b))
    elif operation == "multiply":
        print(multiplication(a,b))
    elif operation == "divide":
        print(division(a,b))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()
