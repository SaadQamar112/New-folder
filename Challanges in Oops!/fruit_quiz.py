import random
class fruit_quiz:
    def __init__(self):
     self.fruits={'apple':'red',
                  'orange':'orange',
                  'watermelon':'green',
                  'banana':'yellow'}
    def quiz(self):
       while True:
          fruit,color=random.choice(list(self.fruits.items()))
          print('what is the color of the fruit',fruit)
          answer=input('enter your answer')
          if (answer==color):
            print("CORRECT")
          else:
             print('INCORRECT')
          option = int(input("enter 0 , if you want to play again otherwise enter 1: "))
          if (option):
             break
print("welcome to fruit quiz ")

fq = fruit_quiz()

fq.quiz()