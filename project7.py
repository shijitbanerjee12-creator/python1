num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")

temp = num1
num1 = num2
num2 = num3
num3 = temp

print(f"After swapping (Method 1): num1 = {num1}, num2 = {num2}, num3 = {num3}")