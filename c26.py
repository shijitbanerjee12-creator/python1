class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
school_bus=bus("School Volvo", 180, 12)
print("Vehicle name : ", school_bus.name, "\n", "Speed : ", school_bus.max_speed, "\n", "Mileage : ", school_bus.mileage, "\n")