from abc import ABC, abstractmethod
class BMW(ABC):
    def slowcar(self):
        print ("BMW is a slow car in comparison to ferrari ")
    def durability(self):
        print ("BMW is a durable car in comparison to ferrari ")
    def peopleschoice(self):
        print ("BMW is a peoples choice car in comparison to ferrari ")
class Ferrari(ABC):
    def fastcar(self):
        print ("Ferrari is a fast car in comparison to bmw ")
    def durability(self):
        print ("Ferrari is not durable car in comparison to bmw ")
    def peopleschoice(self):
        print ("Ferrari is not peoples choice car in comparison to bmw")
obj_bmw = BMW()
obj_ferrari = Ferrari()
for car  in (obj_bmw, obj_ferrari):
    if isinstance(car, BMW):
        car.slowcar()
        car.durability()
        car.peopleschoice()
    elif isinstance(car, Ferrari):
        car.fastcar()
        car.durability()
        car.peopleschoice()
