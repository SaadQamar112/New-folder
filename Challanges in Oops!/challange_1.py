class math:
    def __init__(self,math):
        self.math=math
    def __lt__(self,other):
        if (self.math<other.math):
            return "ob1 is less tan ob2"
        else:
            return "ob2 is less than ob1"
    
    def __eq__(self,other):
        if (self.math==other.math):
            return "value are same"
        else:
            return "the values are different"

obj1=math(8)
obj2=math(2)
print('',obj1,obj2)
print(obj1<obj2)
obj3=math(5)
obj4=math(5)
print('',obj3,obj4)
print(obj3==obj4)
