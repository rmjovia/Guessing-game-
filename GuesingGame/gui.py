
from tkinter import *
import random

attempts = 10
answer = random.randint(1, 99)


def check_answer():
    global attempts
    global text

    attempts -=1

    guess= int (entry_window.get())

    if answer == guess:
        text.set("You win! Congrtas!")

    elif attempts ==0:
        text.set("You are out of attempts")
        btn_check.pack_forget()
    elif guess <  answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Go Higher!!")
    elif guess > answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts remaining - Go Lower!!")
    return


root = Tk()

root.title("Guess the Number")

root.geometry("588x165")

label = Label(root, text= "Guess the number between 1 $ 99")
label.pack()

entry_window = Entry(root, width = 48, borderwidth=4)
entry_window.pack()


btn_check = Button(root, text='Check', command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="quit", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 18 attempts remaining! Good luck!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()


root.mainloop()