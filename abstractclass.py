from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def print(self,x):
        print("the value passed is", x)
    @abstractmethod
    def task(self):
        print("we are in the abstract class")
class test_class(AbstractClass):
    def task(self):
        print("we are in the test class")
test_obj = test_class()
test_obj.task()
test_obj.print(10)           