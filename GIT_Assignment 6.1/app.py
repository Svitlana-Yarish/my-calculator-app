def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Welcome to the Simple Calculator!")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice (1 or 2): ")

if choice in ['1', '2']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
else:
    print("Invalid input! Please select 1 or 2.")