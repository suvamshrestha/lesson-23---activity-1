class person:
    def __init__(self,name, id_no):
        self.name = name
        self.id_no = id_no
    def display(self):
        print("Name:", self.name)
        print("ID No:", self.id_no)
class employee(person):
    def __init__(self, name , id_no, salary, post):
        super().__init__(name, id_no)
        self.salary = salary
        self.post = post
emp = employee("John Doe", "E123", 50000, "Software Engineer")
emp.display()        