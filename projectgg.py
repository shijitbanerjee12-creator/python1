class Dog:

    species = "Canis familiaris"

    def __init__(self, name, breed):
      
        
        self.name = name
        self.breed = breed

    def display_details(self):
     
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {self.species}")
        print("-" *20)

dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog2 = Dog(name="Max", breed="German Shepherd")

print("Details of Dog 1:")
dog1.display_details()

print("Details of Dog 2:")
dog2.display_details()
