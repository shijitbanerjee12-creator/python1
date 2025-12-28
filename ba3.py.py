def check_age(age):
    try:
        age=int(age)
        if age<0:
            raise ValueError("Age cannot be zero")
        if age%2==0:
            print("The age",age,"is even")
        else:
            print("The age",age,"is odd")
    except ValueError as e:
        print("Inavlid age enterd: ",e)
user_input=input("Enter your age: ")
check_age(user_input)