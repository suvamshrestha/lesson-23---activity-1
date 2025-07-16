class IOstring():
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a string: ")
    def print_string(self):
        print("the string is ", self.str1.upper())
str1 = IOstring()
str1.get_string()
str1.print_string()                