from tkinter import *
from random import *

aken=Tk()
aken.title("21 Mäng")
aken.geometry("700x700")
aken.configure(bg="white")
aken.resizable(width=False, height=False)
aken.iconbitmap("cards.ico")

def alusta(event):
    nupp.grid_remove()


for i in range(3):
    aken.grid_rowconfigure(i, weight=1)
    aken.grid_columnconfigure(i, weight=1)


nupp=Button(aken, text="Alusta mängu", bg="lightpink", font=("Arial", 20), fg="black", relief=RAISED, width=30)
nupp.grid(row=1, column=1,pady=20)
nupp.bind("<Button-1>", alusta)


photo=PhotoImage()
# distroe
aken.mainloop()