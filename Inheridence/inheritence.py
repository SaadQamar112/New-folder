class car:
    def __init__(self,maxspeed,milage):
        self.maxspeed=maxspeed
        self.milage=milage
    
class bus (car):
    pass
electric_bus=bus(165,11)

print(electric_bus.maxspeed,electric_bus.milage)
