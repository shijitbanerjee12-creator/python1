try:
    num1, num2=eval(input("Enetr two numbers.Seperated by a comma"))
    result=num1/num2
    print("Result is ",result)
except ZeroDivisionError:
    print("Division by zero is an error !!!")
except SyntaxError:
    print("Comma is missing enter numbers seperated by comma like 1, 2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print()
