class india():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the official language of India")
    def type(self):
        print("India is a self development country")
class USA():
    def capital(self):
        print("Washington D.C. is the capital of the USA")
    def language(self):
        print("English is the official language of the USA")
    def type(self):
        print("USA is a developed country")
obj_ind = india()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
                             