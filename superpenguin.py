class bird:
    def __init__(self):
        print("bird constructor called")
    def fly(self):
        print("bird can fly")
    def sing(self):
        print("bird can sing")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin constructor called")
    def swim(self):
        print("penguin can swim")
    def walk(self):
        print("penguin can walk")
p = penguin()
p.fly()
p.sing()
p.swim()
p.walk()                                