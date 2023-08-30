from tkinter import *
import pandas
import time
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data_dict = pandas.read_csv("data\\remaining_words.csv").to_dict(orient='records')
except FileNotFoundError:
    data_dict = pandas.read_csv("data\\french_words.csv").to_dict(orient='records')
random_word = random.choice(data_dict)
try:
    learned_words = list(pandas.read_csv("data\\learned_words.csv").to_dict(orient='records'))
except FileNotFoundError:
    learned_words = []

def flip_card():
    global random_word
    card.itemconfig(title, text='English',fill='white')
    card.itemconfig(word, text=random_word["English"],fill='white')
    card.itemconfig(card_img, image=card_back)
    
def next_card():    
    global random_word
    card.itemconfig(card_img, image=card_front)
    card.itemconfig(title, text='French',fill='black')
    card.itemconfig(word, text=random_word["French"],fill='black')
    card.after(3000,flip_card)
    
def right():
    global random_word
    learned_words.append(random_word)
    pandas.DataFrame(learned_words).to_csv("data\\learned_words.csv",index=False)
    data_dict.remove(random_word)
    pandas.DataFrame(data_dict).to_csv("data\\remaining_words.csv",index=False)
    random_word = random.choice(data_dict)
    next_card()

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

next_card()


window.mainloop()