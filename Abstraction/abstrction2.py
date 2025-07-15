from abc import ABC,abstractmethod
class human__animal(ABC):
    def move(self):
        pass

class human(human__animal):
    def move(self):
        print('i can run')

class bird(human__animal):
    def move(self):
        print('I can fly')

class horse(human__animal):
    def move(self):
        print('i can run faster')

obj1=human()
obj1.move()
obj2=bird()
obj2.move()
obj3=horse()
obj3.move()
