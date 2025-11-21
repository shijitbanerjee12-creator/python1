m=input("Did you have your medicine Y or N")
a=int(input("Enter your attendence"))
if m=='Y':
    print("You are allowed")
else:
    if a>=75:
        print("Allowed")
    else:
        print("Not allowed")