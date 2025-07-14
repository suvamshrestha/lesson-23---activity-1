class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
species1 = parrot("polly", 3)
species2 = parrot("dolly", 15)
print("polly is a {} ".format(species1.species))
print("dolly is a {} ".format(species2.species))
print("{} is {} years old".format(species1.name, species1.age))
print("{} is {} years old".format(species2.name, species2.age))
