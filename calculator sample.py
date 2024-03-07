def add (x, y) : return x + y
def subtract (x, y) : return x - y
def multiply (x, y) : return x * y
def divide (x, y) :return x / y if y != 0 else "Cannot divide by zero"


num1 = float (input("Enter first number: "))
num2 = float (input("Enter second number: "))
print("/nSelect operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1, 2, 3, or 4:)")
 