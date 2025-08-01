class Roman:
    def convert(self, num):
        roman = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(values)):
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]
        return roman
obj = Roman()
print(obj.convert(58))  

