from string import whitespace
from tkinter import *
from random import randint

root = Tk()

root.title('MRJ - Guessing the number!')

root.geometry("500x500")

num_label = Label(root, text = "pick a number\nBetween 1 and 10!", font =("Brush Script MT", 32))
num_label.pack(pady=20)

def guesser():
    if guess_box.get().isdigit():
        num_label.config(text="pick a number\nBetween 1 and 10!")
        dif = abs(num - int(guess_box.get()))

        #check to see if correct
        if int(guess_box.get())==num:
            bc = 'SystemButtonFace'
            num_label.config(text="Correct!")
        elif dif == 5:
            # set background color to white
            bc = 'white'
        elif dif< 5:
            bc = f'#ff{dif}{dif}{dif}{dif}'
        else:
            bc= f'#{dif}{dif}{dif}{dif}ff'

        #change thr background of the app
        root.config(bg=bc)
        #change bg of the label
        num_label.config(bg=bc)


    else:
        guess_box.delete(0, END)
        num_label.config(text= "hey, that's not a number!")


def rando():
    global num
    num = randint(1, 10)
    #clear the guess box
    guess_box.delete(0, END)
    # change the colors back to normal
    num_label.config(bg = "SystemButtonFace")
    root.config(bg="SystemButtonFace")



guess_box = Entry(root, font = ('Helvetica', 100), width =2)
guess_box.pack(pady=20)

guess_button = Button(root, text= "Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text= "New number", command=rando)
rand_button.pack(pady=20)


#Generate  random number on start
rando()

root.mainloop()
