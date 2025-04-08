from random import randint
import tkinter as tk

platno = tk.Canvas(bg="white",
                   width=500,
                   height=500)
platno.pack()

platno.create_rectangle(50,50,150,250, fill="grey")
platno.create_rectangle(200,50,300,250, fill="grey")
platno.create_rectangle(350,50,450,250, fill="grey")

farby = ["yellow", "red", "blue","green","orange", "pink"]


def Animacia():
    global nahoda, farby, ConstNahoda
    platno.delete("num0")
    platno.delete("num1")
    platno.delete("num2")
    
    pole = []
    for i in range(3):
        cislo = randint(1,9)
        pole.append(cislo)
        platno.create_text(100 + i*150, 150, fill=farby[randint(0,5)], text=cislo, font=("Purisa", 50), tag="num"+str(i))
    if nahoda == 0:
        Vysledok(pole)
        return
    nahoda -= 1

    platno.after(100, Animacia)

def Start():
    global nahoda, ConstNahoda, peniaze
    platno.delete("p")
    peniaze -= 1
    nahoda = randint(2,10)
    nahoda = nahoda * 3
    ConstNahoda = nahoda
    platno.create_text(50,300, text="Peniaze: " + str(peniaze), tag="p")
    Animacia()    

def Vysledok(roll):
    if roll[0] == roll[1] == roll[2]:
        print("yayyy")
    else:
        print("Nayy")
    
peniaze = 100
button1 = tk.Button(text="Start",
                    command=Start,
                    width=15,
                    height=3)
button1.pack()
