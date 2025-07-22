class Reverse:
    def __init__(self, text):
        self.text = text
    def reverse_words(self):
        words = self.text.split()
        result = ""
        for word in words:
            result += word[::-1] + " "
        return result.strip()
user_text = input("Enter a sentence: ")
rev = Reverse(user_text)
print("Reversed words:", rev.reverse_words())
