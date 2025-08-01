class Converter:
    def __init__(self):
        self.values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    def to_roman(self, number):
        result = ""
        for val, symbol in self.values:
            while number >= val:
                result += symbol
                number -= val
        return result
c = Converter()
print(c.to_roman(2025))  
