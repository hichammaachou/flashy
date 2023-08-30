from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

card_front = PhotoImage(file='images/card_front.png')
right_img= PhotoImage(file='images/right.png')
wrong_img= PhotoImage(file='images/wrong.png')
card = Canvas(window,width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card.create_image(400,263,image=card_front)
card.create_text(400,150,text='French',font=("Ariel",40,"italic"))
card.create_text(400,263,text='Word',font=("Ariel",60,"bold"))
card.grid(row=0,column=0,columnspan=3)

wrong = Button(image=wrong_img,relief='flat',borderwidth=0,command=right)
wrong.grid(row=1,column=0)
right = Button(image=right_img,relief='flat',borderwidth=0,command=right)
right.grid(row=1,column=2)
window.mainloop()