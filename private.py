class myClass:
    __privateVar = 42;
    def __privMeth(self):
        print("This is a private method.")
    def hello(self):
        print("private variable value ", myClass.__privateVar)
car = myClass()
car.hello()
car.__privMeth()  # This will raise an AttributeError


