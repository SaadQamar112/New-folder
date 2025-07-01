class Dog:
    species='Animal'
    def __init__(self,name,hight):
        self.name=name
        self.hight=hight

Nami=Dog('Nami',3.11)
UNI=Dog('UNI',3.12)

print('Nami is a {}'.format(Nami.species))
print('UNI is a {}'.format(UNI.species))

print('{} is {} feet'.format(Nami.name,Nami.hight))
print('{} is {} feet'.format(UNI.name,UNI.hight))