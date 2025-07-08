class person(object):
    def __init__(self,name,National_ID):
        self.name=name
        self.National_ID=National_ID
    def display(self):
        print(self.name)
        print(self.National_ID)

class employee(person):
    def __init__(self,name,National_ID,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,National_ID)
BI=employee('Sam',123456780,50000,'manager')
BI.display()
print(BI.salary)
print(BI.post)
