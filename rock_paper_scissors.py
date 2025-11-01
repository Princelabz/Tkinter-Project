
from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors Game")

Label(root, text="Rock 🗿 Paper 📜 Scissors ✂").grid(row=0, column=1)
Label(root , text="1-Rock, 2-Paper, 3-Scissors").grid(row=2, column=0)
Label(root, text="Enter Your Choice :").grid(row=3 ,column=0)
e1 = Entry(root)
e1.grid(row=3, column=1)

result_label = Label(root, text="")
result_label.grid(row=6, column=0, columnspan=3)

def Submitfuc():
    try:
        user_choice = int(e1.get()) 
        if user_choice < 1 or user_choice > 3:
            result_label.config(text="Please enter a number between 1 and 3!")
            return

        computer_choice = random.randint(1, 3)

        if user_choice == computer_choice:
            result = "Tie!"
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            result = "You Win!"
        else:
            result = "You Lose!"

        result_label.config(text=f"Computer chose {computer_choice}. {result}")

    except ValueError:
        result_label.config(text="Please enter a valid number!")

def clear_entry():
    e1.delete(0,END)

button1 = Button(root, text="🗿 Rock", command=lambda: e1.insert(0, "1"))
button1.grid(row=4, column=0)
button2 = Button(root, text="📜 Paper", command=lambda: e1.insert(0, "2"))
button2.grid(row=4, column=1)
button3 = Button(root, text="✂ Scissors", command=lambda: e1.insert(0, "3"))
button3.grid(row=4, column=2)

submit = Button(root, text="Submit", command=Submitfuc)
submit.grid(row=5, column=1)

clear = Button(root, text="Clear", command=clear_entry)
clear.grid(row=5, column=0)

root.mainloop()
