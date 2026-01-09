import random
playing = True
number = str(random.randint(10,20))
print("I will generate a number between 10- 20, and you will have to guess it one digit at a time")
print("The game ends when you get 1 hero!")
while playing:
    guess=input("Give me your best guess \n")
    if number==guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("sorry, wrong guess, try again")
       