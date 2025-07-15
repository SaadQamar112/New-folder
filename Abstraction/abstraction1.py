from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("we are inside of  abstract method class")

class subclass(Absclass):
    def task(self):
        print('we are inside of the sub task class')

objtask=subclass()
objtask.task()
objtask.print(30)
