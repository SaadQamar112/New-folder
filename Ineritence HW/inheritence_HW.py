class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (0.1 * base_fare)
        return total_fare

bus1 = Bus("School Bus", 50)
print("Total bus fare:", bus1.fare())
