
class parrot:
    species='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age

poplu=parrot('poplu',4)
coding=parrot('coding',10)

print('poplu is a {}'.format(poplu.species))
print('coding is a {}'.format(coding.species))

print('{} is {} years old'.format(poplu.name,poplu.age))
print('{} is {} years old'.format(coding.name,coding.age))