from tkinter import *
import random

aken=Tk()
aken.title("21 Mäng")
aken.geometry("700x700")
aken.configure(bg="white")
aken.resizable(width=False, height=False)
aken.iconbitmap("cards.ico")

def alusta(event):
    nupp.grid_remove()
    pilt_1.grid(row=15, column=0, pady=20, padx=5, rowspan=4, columnspan=3)
    pilt_2.grid(row=15, column=1, pady=20, padx=5, rowspan=4, columnspan=3)
    s.grid(row=15, column=3, pady=5, padx=5, rowspan=4, columnspan=3)
    lisa_nupp.grid(row=16, column=3, pady=20, padx=5, rowspan=4, columnspan=3)
    end_nupp.grid(row=17, column=3, pady=20, padx=5, rowspan=4, columnspan=3)

def valik1()-> any:
    koik=0
    fail="cards.txt"
    with open(fail, 'r', encoding="utf-8-sig") as f:
        cards=[]
        for rida in f:
            cards.append(eval(rida.strip()))
    random.shuffle(cards)
    valitud=cards[:1]
    for kirje in valitud:
        h=kirje
    card=["ch", "x", "b", "p"]
    b=random.choice(card)
    c=h[b]
    f=h["k"]
    return c, f

def valik2()-> any:
    koik=0
    fail="cards.txt"
    with open(fail, 'r', encoding="utf-8-sig") as f:
        cards=[]
        for rida in f:
            cards.append(eval(rida.strip()))
    random.shuffle(cards)
    valitud=cards[:1]
    for kirje in valitud:
        h=kirje
    card=["ch", "x", "b", "p"]
    d=random.choice(card)
    k=h[d]
    r=h["k"]
    return k, r


for i in range(3):
    aken.grid_rowconfigure(i, weight=1)
    aken.grid_columnconfigure(i, weight=1)


nupp=Button(aken, text="Alusta mängu", bg="lightpink", font=("Arial", 20), fg="black", relief=RAISED, width=30)
nupp.grid(row=1, column=1,pady=20)
nupp.bind("<Button-1>", alusta)
lisa_nupp=Button(aken, text="VEEL", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=30)
end_nupp=Button(aken, text="LOPETA VOOR", bg="lightblue", font=("Arial", 12), fg="black", relief=RAISED, width=30)

card1, arv1=valik1()
card2, arv2=valik2()
summa=arv1 + arv2
s=Label(aken, text=(f"Summa: {summa}"),  bg="white", font=("Arial", 17), fg="black",width=10, height=1 )
picture1=PhotoImage(file=card1)
picture2=PhotoImage(file=card2)
pilt_1=Label(aken,image=picture1)
pilt_2=Label(aken,image=picture2)
pilt_1.image = picture1
pilt_2.image = picture2

photo=PhotoImage()
# distroe
aken.mainloop()

# from tkinter import *
# import random

# aken = Tk()
# aken.title("21 Mäng")
# aken.geometry("700x700")
# aken.configure(bg="white")
# aken.resizable(width=False, height=False)
# aken.iconbitmap("cards.ico")

# def alusta(event):
#     nupp.grid_remove()
#     card1 = valik1()
#     card2 = valik2()
#     picture1 = PhotoImage(file=card1)
#     picture2 = PhotoImage(file=card2)
    
#     # Сохранение изображений, чтобы не потерять ссылки
#     pilt_1 = Label(aken, image=picture1)
#     pilt_1.grid(row=40, column=1, pady=20)
#     pilt_2 = Label(aken, image=picture2)
#     pilt_2.grid(row=40, column=2, pady=20)
    
#     # Сохраняем изображения, чтобы они не были удалены
#     pilt_1.image = picture1
#     pilt_2.image = picture2

# def valik1() -> any:
#     fail = "cards.txt"
#     with open(fail, 'r', encoding="utf-8-sig") as f:
#         cards = []
#         for rida in f:
#             cards.append(eval(rida.strip()))  # Строки преобразуются в словари
#     random.shuffle(cards)  # Перемешиваем карты
#     valitud = cards[:1]  # Выбираем первую карту
#     for kirje in valitud:
#         h = kirje  # Это будет словарь, например {"ch": "2c.PNG", "x": "2x.PNG", "b": "2b.PNG", "p": "2p.PNG"}
    
#     card = ["ch", "x", "b", "p"]  # Список ключей для карты
#     b = random.choice(card)  # Случайным образом выбираем один из ключей
    
#     # Получаем значение по выбранному ключу
#     c = h[b]
    
#     return c

# def valik2() -> any:
#     fail = "cards.txt"
#     with open(fail, 'r', encoding="utf-8-sig") as f:
#         cards = []
#         for rida in f:
#             cards.append(eval(rida.strip()))  # Строки преобразуются в словари
#     random.shuffle(cards)  # Перемешиваем карты
#     valitud = cards[:1]  # Выбираем первую карту
#     for kirje in valitud:
#         h = kirje  # Это будет словарь, например {"ch": "2c.PNG", "x": "2x.PNG", "b": "2b.PNG", "p": "2p.PNG"}
    
#     card = ["ch", "x", "b", "p"]  # Список ключей для карты
#     d = random.choice(card)  # Случайным образом выбираем один из ключей
    
#     # Получаем значение по выбранному ключу
#     k = h[d]
    
#     return k

# # Настройка сетки
# for i in range(3):
#     aken.grid_rowconfigure(i, weight=1)
#     aken.grid_columnconfigure(i, weight=1)

# # Кнопка для начала игры
# nupp = Button(aken, text="Alusta mängu", bg="lightpink", font=("Arial", 20), fg="black", relief=RAISED, width=30)
# nupp.grid(row=1, column=1, pady=20)
# nupp.bind("<Button-1>", alusta)

# aken.mainloop()
