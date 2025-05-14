from tkinter import *
import random

aken=Tk()
aken.title("21 Mäng")
aken.geometry("700x700")
aken.configure(bg="white")
aken.resizable(width=False, height=False)
aken.iconbitmap("joker.ico")

def alusta(event):
    nupp.grid_remove()
    pilt_1.grid(row=15, column=0, pady=20, padx=10, rowspan=3, columnspan=3)
    pilt_2.grid(row=15, column=1, pady=20, padx=10, rowspan=3, columnspan=3)
    s.grid(row=15, column=3, pady=5, padx=10, rowspan=3, columnspan=3)
    lisa_nupp.grid(row=16, column=3, pady=20, padx=10, rowspan=3, columnspan=3)
    end_nupp.grid(row=17, column=3, pady=20, padx=10, rowspan=3, columnspan=3)
    stop_nupp.grid(row=18, column=3, pady=20, padx=10, rowspan=3, columnspan=3)

def valik1()-> any:
    fail1="-cards.txt"
    with open (fail1, 'r', encoding="utf-8-sig") as f:
        c=[]
        for rida in f:
            c.append(eval(rida.strip()))
    koik=0
    fail="cards.txt"
    with open(fail, 'r', encoding="utf-8-sig") as f:
        cards=[]
        for rida in f:
            cards.append(eval(rida.strip()))
    g=random.choice(cards)
    card=["ch", "x", "b", "p"]
    b=random.choice(card)
    uus_card={'card': g[b]}
    while 1:
        if b in c:
            g=random.choice(cards)
            card=["ch", "x", "b", "p"]
            b=random.choice(card)
            uus_card={'card': g[b]}
        else:
            with open(fail1, 'a', encoding="utf-8-sig") as f:
                f.write(str(uus_card)+'\n')
            break
    c=g[b]
    h=g["k"]
    return c, h

def valik2()-> any:
    fail1="-cards.txt"
    with open (fail1, 'r', encoding="utf-8-sig") as f:
        c=[]
        for rida in f:
            c.append(eval(rida.strip()))
    koik=0
    fail="cards.txt"
    with open(fail, 'r', encoding="utf-8-sig") as f:
        cards=[]
        for rida in f:
            cards.append(eval(rida.strip()))
    g=random.choice(cards)
    card=["ch", "x", "b", "p"]
    b=random.choice(card)
    uus_card={'card': g[b]}
    while 1:
        if b in c:
            g=random.choice(cards)
            card=["ch", "x", "b", "p"]
            b=random.choice(card)
            uus_card={'card': g[b]}
        else:
            with open(fail1, 'a', encoding="utf-8-sig") as f:
                f.write(str(uus_card)+'\n')
            break
    p=g[b]
    k=g["k"]
    return p,k

def veel (event):
    summa=int(arv1)+int(arv2)+int(arv3)
    s=Label(aken, text=(f"Summa: {summa}"),  bg="white", font=("Arial", 17), fg="black",width=15, height=1 )
    pilt_1.grid(row=15, column=0, pady=20, padx=10, rowspan=3, columnspan=3)
    pilt_2.grid(row=15, column=1, pady=20, padx=10, rowspan=3, columnspan=3)
    pilt_3.grid(row=15, column=2, pady=20, padx=10, rowspan=3, columnspan=3)
    s.grid(row=15, column=3, pady=5, padx=10, rowspan=3, columnspan=3)
    lisa_nupp.grid(row=16, column=3, pady=20, padx=10, rowspan=3, columnspan=3)
    end_nupp.grid(row=17, column=3, pady=20, padx=10, rowspan=3, columnspan=3)

for i in range(3):
    aken.grid_rowconfigure(i, weight=1)
    aken.grid_columnconfigure(i, weight=1)

       

nupp=Button(aken, text="Alusta mängu", bg="lightpink", font=("Arial", 20), fg="black", relief=RAISED, width=30)
nupp.grid(row=1, column=1,pady=20)
nupp.bind("<Button-1>", alusta)
lisa_nupp=Button(aken, text="VEEL", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=30)
end_nupp=Button(aken, text="LOPETA VOOR", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=30)
stop_nupp=Button(aken, text="STOP", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=30 )

card1, arv1=valik1()
card2, arv2=valik2()
card3, arv3=valik3()
summa=int(arv1) + int(arv2)
s=Label(aken, text=(f"Summa: {summa}"),  bg="white", font=("Arial", 17), fg="black",width=15, height=1 )
picture1=PhotoImage(file=card1)
picture2=PhotoImage(file=card2)
picture3=PhotoImage(file=card3)
pilt_1=Label(aken,image=picture1)
pilt_2=Label(aken,image=picture2)
pilt_3=Label(aken,image=picture3)
pilt_1.image = picture1
pilt_2.image = picture2
pilt_3.image = picture3

photo=PhotoImage()
# distroe
aken.mainloop()


