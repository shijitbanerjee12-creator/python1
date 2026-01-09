import random
options=["Rock","Paper","Scissor"]
user_choice=input("Choose Rock, Paper or Scissor: ")
computer_choice=random.choice(options)
print("You choose",user_choice)
print("Computer chose",computer_choice)
if user_choice==computer_choice:
    print("It is a tie")
elif user_choice=="Rock" and computer_choice=="Scissor":
    print("You win")
elif user_choice=="Scissor"and computer_choice=="Paper":
    print("You win")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("You win")
else:
    print("You lose")