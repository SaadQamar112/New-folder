class lambo():
    def speed(self):
        print('my speed goes 350km ')
    def texture(self):
        print('my texture is the best')
    def petrol(self):
        print('i take to much petrol')

class ferarie():
    def speed(self):
        print('my speed goes 250km')
    def texture(self):
        print('my texture is very good')
    def petrol(self):
        print('i take medium amount of petrol')

obj1=lambo()
obj2=ferarie()
for car in(obj1,obj2):
    car.speed()
    car.texture()
    car.petrol()
