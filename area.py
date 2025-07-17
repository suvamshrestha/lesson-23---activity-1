class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416
    def area(self):
        return self.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * self.pi * self.radius
r = float(input("Enter the radius of the circle: "))
c = Circle(r)
print("Area:", round(c.area(), 2))
print("Perimeter:", round(c.perimeter(), 2))
