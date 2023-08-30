from tkinter import *
import pandas
import time
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data\\french_words.csv")
data_dict =data.to_dict(orient='records')
random_word = random.choice(data_dict)
def to_eng():
    global random_word
    card.itemconfig(title, text='English',fill='white')
    card.itemconfig(word, text=random_word["English"],fill='white')
    card.itemconfig(card_img, image=card_back)
    random_word = random.choice(data_dict)
def right():    
    card.itemconfig(card_img, image=card_front)
    card.itemconfig(title, text='French',fill='black')
    card.itemconfig(word, text=random_word["French"],fill='black')
    card.after(3000,to_eng)
    
    

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
right_img= PhotoImage(file='images/right.png')
wrong_img= PhotoImage(file='images/wrong.png')
card = Canvas(window,width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img = card.create_image(400,263,image=card_front)
title = card.create_text(400,150,text='',font=("Ariel",40,"italic"))
word = card.create_text(400,263,text='',font=("Ariel",60,"bold"))
card.grid(row=0,column=0,columnspan=3)

wrong = Button(window,image=wrong_img,relief='flat',borderwidth=0,highlightthickness=0,command=right)
wrong.grid(row=1,column=0)
right_button = Button(window,image=right_img,relief='flat',borderwidth=0,highlightthickness=0,command=right)
right_button.grid(row=1,column=2)

right()


window.mainloop()