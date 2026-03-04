class Ferrari:
    def fuel_type(self):
         print("Fuel type: Petrol")
    def max_speed(self):
        print("Max speed: 350 mph")
class BMW:
    def fuel_type(self):
      print("Fuel type: Diesel")
    def max_speed(self):
        print("Max speed: 240 mph")
def car_details(car_object):
    print(f"\n--- Details for a {type(car_object).__name__} ---")
    car_object.fuel_type()
    car_object.max_speed()
ferrari_obj = Ferrari()
bmw_obj = BMW()
car_details(ferrari_obj)
car_details(bmw_obj)
print("\n--- Iterating through car objects ---")
for car in (ferrari_obj, bmw_obj):
    car.fuel_type()
    car.max_speed()
