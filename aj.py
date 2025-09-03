import tkinter as tk
import random
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
    user_choice_label.config(text=f"Your Choice: {choice}")
    comp_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.config(bg="lightblue")
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)
user_choice_label = tk.Label(root, text="Your Choice: None", font=("Arial", 12), bg="lightblue")
user_choice_label.pack()
comp_choice_label = tk.Label(root, text="Computer's Choice: None", font=("Arial", 12), bg="lightblue")
comp_choice_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="darkred", bg="lightblue")
result_label.pack(pady=10)
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()
rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)
root.mainloop()
