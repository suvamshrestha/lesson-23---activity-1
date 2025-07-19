class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehicle):
    pass
school_bus = bus("School Volvo", 180, 12)
print("vehicle name:", school_bus.name)
print("Max speed:", school_bus.max_speed, "km/h")
print("Mileage:", school_bus.mileage, "km/l")
