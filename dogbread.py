class Dog:
    animal = "dog"
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
dog1 = Dog("Labrador", "Black")
dog2 = Dog("Beagle", "Brown")
dog1.display_details()
dog2.display_details()
