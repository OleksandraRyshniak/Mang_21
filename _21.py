from tkinter import *
import random

summa = 0
summa_robot = 0
pilt=[]
pilt_robot=[]
mangija_voidud = 0
robot_voidud = 0
kaartide_arv = 0


aken=Tk()
aken.title("21 Mäng")
aken.geometry("700x850")
aken.configure(bg="white")
aken.resizable(width=False, height=False)
aken.iconbitmap("joker.ico")


def login0(event):
    login_=login.get()
    if not login_:
        login.config( bg="red", font=("Arial",20), fg="black", width=25)
        return
    alusta()

def alusta():
    nupp.place_forget()
    sisesta.place_forget()
    login.place_forget()
    pilt_1.grid(row=23, column=0, pady=5, padx=5,rowspan=5) 
    pilt_2.grid(row=23, column=1, pady=5, padx=5,rowspan=5)
    s.grid(row=21, column=3, pady=1, padx=10)      
    lisa_nupp.grid(row=22, column=3, pady=1, padx=10)  
    end_nupp.grid(row=23, column=3, pady=1, padx=10)
    start_nupp.grid(row=24, column=3, pady=1, padx=10)
    stop_nupp.grid(row=25, column=3, pady=1, padx=10)
    kogus_label.grid(row=5, column=3)
    kogus_robot_label.grid(row=6, column=3)
    tulemus_label.grid(row=7, column=3)

def valik()-> any:
    fail1="cards7.txt"
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
    uus_card={b: g[b]}
    while 1:
        if uus_card in c:
            g=random.choice(cards)
            card=["ch", "x", "b", "p"]
            b=random.choice(card)
            uus_card={b: g[b]}
        else:
            with open(fail1, 'a', encoding="utf-8-sig") as f:
                f.write(str(uus_card)+'\n')
            break
    c=g[b]
    h=g["k"]
    return c, h

def veel (event):
    global summa, kaartide_arv, pilt  
    if kaartide_arv >= 5:
        return  
    card, arv = valik()
    picture = PhotoImage(file=card)
    pilt_ = Label(aken, image=picture)
    pilt_.image = picture
    pilt_.grid(row=18, column=kaartide_arv, pady=5, padx=5, rowspan=5)
    pilt.append(pilt_)  
    summa += int(arv)
    s.config(text=(f"Summa: {summa}"))
    kaartide_arv += 1

def end(event):
    global summa_robot, summa, mangija_voidud, robot_voidud, pilt_robot
    lisa_nupp.grid_remove()
    end_nupp.grid_remove()
    login_ = login.get()
    pilt_robot_1.grid(row=0, column=0, pady=5, padx=5)
    pilt_robot_2.grid(row=0, column=1, pady=5, padx=5)
    su.grid(row=0, column=3, pady=5, padx=10)
    if summa_robot < 17:
        card_robot_3, arv_3 = valik()
        picture_robot_3 = PhotoImage(file=card_robot_3)
        pilt_robot_3 = Label(aken, image=picture_robot_3)
        pilt_robot_3.image = picture_robot_3
        pilt_robot_3.grid(row=0, column=2, pady=5, padx=5)
        summa_robot += int(arv_3)
        su.config(text=(f"Summa: {summa_robot}"))
        pilt_robot.append(pilt_robot_3)
    if summa_robot < 21:
        card_robot_4, arv_4 = valik()
        picture_robot_4 = PhotoImage(file=card_robot_4)
        pilt_robot_4 = Label(aken, image=picture_robot_4)
        pilt_robot_4.image = picture_robot_4
        pilt_robot_4.grid(row=1, column=0, pady=5, padx=5)
        summa_robot += int(arv_4)
        su.config(text=f"Summa: {summa_robot}")
        pilt_robot.append(pilt_robot_4)
    if summa_robot < 21:
        card_robot_5, arv_5 = valik()
        picture_robot_5 = PhotoImage(file=card_robot_5)
        pilt_robot_5 = Label(aken, image=picture_robot_5)
        pilt_robot_5.image = picture_robot_5
        pilt_robot_5.grid(row=1, column=1, pady=5, padx=5)
        summa_robot += int(arv_5)
        su.config(text=f"Summa: {summa_robot}")
        pilt_robot.append(pilt_robot_5)
    if summa > 21 and summa_robot > 21:
        tulemus = "Viik" 
    elif summa > 21:
        tulemus = "Robot võitis"
        robot_voidud += 1
    elif summa_robot > 21:
        tulemus = f"{login_} võitis"
        mangija_voidud += 1
    elif summa > summa_robot:
        tulemus = f"{login_} võitis"
        mangija_voidud += 1
    elif summa < summa_robot:
        tulemus = "Robot võitis"
        robot_voidud += 1
    else:
        tulemus = "Viik" 
    tulemus_label.config(text=tulemus)
    tulemus_label.grid(row=7, column=3)
    kogus_label.config(text=(f"Tulemus {login_}: {mangija_voidud}"))
    kogus_label.grid(row=5, column=3)
    kogus_robot_label.config(text=(f"Tulemus robot: {robot_voidud}"))
    kogus_robot_label.grid(row=6, column=3)

def alustar(event):
    global picture1, picture2, picture_robot_1, picture_robot_2
    global pilt_1, pilt_2, pilt_robot_1, pilt_robot_2
    global summa, summa_robot, pilt, pilt_robot, kaartide_arv
    with open("cards7.txt", 'w', encoding="utf-8-sig") as f:
        pass
    kaartide_arv = 0
    for kaart in pilt:
        kaart.grid_forget()
    for kaart in pilt_robot:
        kaart.grid_forget()
    pilt.clear()
    pilt_robot.clear()
    card1, arv1 = valik()
    card2, arv2 = valik()
    summa = int(arv1) + int(arv2)
    picture1 = PhotoImage(file=card1)
    picture2 = PhotoImage(file=card2)
    pilt_1.config(image=picture1)
    pilt_1.image = picture1
    pilt_2.config(image=picture2)
    pilt_2.image = picture2
    pilt_1.grid(row=23, column=0, pady=5, padx=5, rowspan=5)
    pilt_2.grid(row=23, column=1, pady=5, padx=5, rowspan=5)
    s.config(text=f"Summa: {summa}")
    su.config(text="")
    card_robot_1, arv_1 = valik()
    card_robot_2, arv_2 = valik()
    summa_robot = int(arv_1) + int(arv_2)
    picture_robot_1 = PhotoImage(file=card_robot_1)
    picture_robot_2 = PhotoImage(file=card_robot_2)
    pilt_robot_1.config(image=picture_robot_1)
    pilt_robot_1.image = picture_robot_1
    pilt_robot_2.config(image=picture_robot_2)
    pilt_robot_2.image = picture_robot_2
    pilt.append(pilt_1 )
    pilt.append(pilt_2 )
    pilt_robot.append(pilt_robot_1)
    pilt_robot.append(pilt_robot_2)
    tulemus_label.config(text="")
    lisa_nupp.grid(row=22, column=3, pady=1, padx=10)
    end_nupp.grid(row=23, column=3, pady=1, padx=10)

def exit(event):
    fail="tulemus.txt"
    login_=login.get()
    mangija_score = mangija_voidud
    robot_score = robot_voidud
    uus={login_: mangija_score, 'robot': robot_score}
    aken.destroy()
    with open (fail, 'a', encoding="utf-8-sig") as f:
        f.write(str(uus)+'\n')
    aken1=Tk()
    aken1.title("21 Mäng")
    aken1.geometry("500x500")
    aken1.configure(bg="white")
    aken1.resizable(width=False, height=False)
    aken1.iconbitmap("joker.ico")
    skoor_mängija = Label(aken1, text=f"{login_}: {mangija_score}", font=("Arial", 16), bg="white")
    skoor_mängija.pack(pady=10)
    skoor_robot = Label(aken1, text=f"Robot: {robot_score}", font=("Arial", 16), bg="white")
    skoor_robot.pack(pady=10)
    sulge_nupp = Button(aken1, text="SULGE", font=("Arial", 14), command=aken1.destroy)
    sulge_nupp.pack(pady=20)
    ajalugu_nupp=Button(aken1, text="AJALUGU", font=("Arial", 14))
    ajalugu_nupp.bind("<Button-1>", ajalugu)
    ajalugu_nupp.pack(pady=20)
    with open("cards7.txt", 'w', encoding="utf-8-sig") as f:
        pass  

def ajalugu(event):
    aken2 = Tk()
    aken2.title("Ajalugu – 21 Mäng")
    aken2.geometry("500x500")
    aken2.configure(bg="white")
    aken2.resizable(width=False, height=False)
    aken2.iconbitmap("joker.ico")
    try:
        with open("tulemus.txt", 'r', encoding="utf-8-sig") as f:
            tulemused = []
            for rida in f:
                rida = rida.strip()
                if rida:
                    tulemus = eval(rida) 
                    tulemused.append(tulemus)
    except:
        tulemused = []
    if not tulemused:
        tekst = Label(aken2, text="Tulemusi pole veel.", bg="white", font=("Arial", 14))
        tekst.pack(pady=20)
    else:
        for i, tulemus in enumerate(tulemused, start=1):
            tekst = f"{i}. "
            for votsi, vaartus in tulemus.items():
                tekst += f"{votsi}: {vaartus}  "
            lbl = Label(aken2, text=tekst, bg="white", font=("Arial", 12), anchor="w", justify=LEFT)
            lbl.pack(anchor="w", padx=20)

for i in range(5):
    aken.grid_rowconfigure(i, weight=1)
    aken.grid_columnconfigure(i, weight=1)

kogus_label = Label(aken, text="Tulemus: 0", bg='white', font=("Arial", 15))
kogus_robot_label = Label(aken, text="Tulemus robot: 0", bg='white', font=("Arial", 15))
tulemus_label = Label(aken, text="", bg='white', font=("Arial", 15))
login=Entry(aken, bg='lightblue', font=("Arial", 20), fg="black", width=25)
login.place(relx=0.4, rely=0.60, anchor="center")
sisesta=Label(aken, text="Sisesta oma login: ", bg='white', font=("Arial", 20), fg="black")
sisesta.place(relx=0.3, rely=0.50, anchor="center")
nupp=Button(aken, text="Alusta mängu", bg="lightpink", font=("Arial", 20), fg="black", relief=RAISED, width=30)
nupp.place(relx=0.5, rely=0.40, anchor="center")
nupp.bind("<Button-1>" , login0)
lisa_nupp=Button(aken, text="VEEL", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=15)
lisa_nupp.bind("<Button-1>", veel)
end_nupp=Button(aken, text="LOPETA VOOR", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=15)
end_nupp.bind("<Button-1>", end)
stop_nupp=Button(aken, text="STOP", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=15 )
stop_nupp.bind("<Button-1>", exit)
start_nupp=Button(aken,text="ALUSTA VOOR", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=15)
start_nupp.bind("<Button>", alustar)

card1, arv1=valik()
card2, arv2=valik()
card_robot_1, arv_1=valik()
card_robot_2, arv_2=valik()
summa=int(arv1) + int(arv2) 
summa_robot=int(arv_1) + int(arv_2)
su=Label(aken, text=(f"Summa: {summa_robot}"),  bg="white", font=("Arial", 17), fg="black",width=15, height=1 )
s=Label(aken, text=(f"Summa: {summa}"),  bg="white", font=("Arial", 17), fg="black",width=15, height=1 )
picture1=PhotoImage(file=card1)
picture2=PhotoImage(file=card2)
pilt_1=Label(aken,image=picture1)
pilt_2=Label(aken,image=picture2)
picture_robot_1=PhotoImage(file=card_robot_1)
picture_robot_2=PhotoImage(file=card_robot_2)
pilt_robot_1=Label(aken, image=picture_robot_1 )
pilt_robot_2=Label(aken, image=picture_robot_2 )
pilt_1.image = picture1
pilt_2.image = picture2
pilt_robot_1.image= picture_robot_1
pilt_robot_2.image= picture_robot_2
pilt.append(pilt_1 )
pilt.append(pilt_2 )
pilt_robot.append(pilt_robot_1)
pilt_robot.append(pilt_robot_2)

aken.mainloop()


