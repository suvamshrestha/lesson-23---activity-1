import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "apple":"red", "banana":"yellow", "watermelon":"green",
            "orange":"orange", "grape":"purple", "kiwi":"brown",  
        }
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the color of the fruit?".format(fruit))
            user_answer = input()
            if (user_answer.lower() == color):
                print("Correct!")
            else:
                print("Incorrect! ")
            option = int(input("Do you want to continue? (1 for no, 0 for yes): "))
            if option == 1:
                print("Thank you for playing!")
                break
            elif option == 0:
                continue
            else:
                print("Invalid option, exiting the quiz.")
                break
            

            
            
        