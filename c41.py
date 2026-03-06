import random
class FruitQuiz:
    def __init__(self):
        self.fruit={'apple':'red',
                    'orange':'orange',
                    'watermeon':'green',
                    'banana':'yellow'}
    def quiz(self):
        while (True):
            fruit, colour=random.choice(list(self.fruit.items()))
            print("What is the colour of{}".format(fruit))
            user_answer=input()
            if user_answer.lower()==colour:
                print("Correct answer")
            else:
                print("Incorrect answer")
            option=int(input("Enter 0 if you want to continue and 0 if you want to end the game"))
            if(option):
                break
print("Welcome to fruit quiz")
fq=FruitQuiz()
fq.quiz()
