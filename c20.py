class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
x=int(input("Enter maximum speed for mode 1 : "))
y=int(input("Enter mileage for mode 1 : "))
mode1X = vehicle(x,y)
print(" Mode 1 maximun speed", mode1X.max_speed)
print(" Mode 1 mileage", mode1X.mileage)        