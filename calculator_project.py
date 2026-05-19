# Calculator Project

# Addition Function
def add(a, b):
    return a + b


# Subtraction Function
def subtract(a, b):
    return a - b


# Multiplication Function
def multiply(a, b):
    return a * b


# Division Function
def divide(a, b):
    return a / b


# User se numbers lena
num1 = float(input("First number likho: "))
num2 = float(input("Second number likho: "))

# Operations show karna
print("\nChoose Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Apni choice likho (1/2/3/4): ")

# Conditions
if choice == "1":
    print("Answer:", add(num1, num2))

elif choice == "2":
    print("Answer:", subtract(num1, num2))

elif choice == "3":
    print("Answer:", multiply(num1, num2))

elif choice == "4":
    print("Answer:", divide(num1, num2))

else:
    print("Invalid Choice")