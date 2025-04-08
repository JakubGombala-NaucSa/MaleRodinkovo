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
    global nahoda, farby, ConstNahoda, vysledky
    if ConstNahoda - nahoda < ConstNahoda/3:
        platno.delete("num0")
        cislo = randint(1,9)
        platno.create_text(100, 150, fill=farby[randint(0,5)], text=cislo, font=("Purisa", 50), tag="num0")
        vysledky[0] = cislo
    if ConstNahoda - nahoda < ConstNahoda*2/3:
        platno.delete("num1")
        cislo = randint(1,9)
        platno.create_text(250, 150, fill=farby[randint(0,5)], text=cislo, font=("Purisa", 50), tag="num1")
        vysledky[1] = cislo
    if ConstNahoda - nahoda < ConstNahoda:
        platno.delete("num2")
        cislo = randint(1,9)
        platno.create_text(400, 150, fill=farby[randint(0,5)], text=cislo, font=("Purisa", 50), tag="num2")
        vysledky[2] = cislo
        
    if nahoda == 0:
        Vysledok(vysledky)
        return
    nahoda -= 1

    platno.after(100, Animacia)

def Start():
    global nahoda, ConstNahoda, peniaze, vysledky
    vysledky = [0,0,0]
    platno.delete("p")
    peniaze -= 1
    nahoda = randint(2,10)
    nahoda = nahoda * 3
    ConstNahoda = nahoda
    platno.create_text(50,300, text="Peniaze: " + str(peniaze), tag="p")
    Animacia()    

def Vysledok(roll):
    if roll[0] == roll[1] == roll[2] and roll[0] == 7:
        peniaze += 10
    elif roll[0] == roll[1] == roll[2]:
        peniaze += 3
    elif roll[0]+2 == roll[1]+1 == roll[2]:
        peniaze += 6
    elif ((roll[0] == roll[1] and roll[0] == 7) or
         (roll[0] == roll[2] and roll[0] == 7) or
         (roll[1] == roll[2] and roll[1] == 7)):
        peniaze += 5
    elif roll[0] == 7 or roll[1] == 7 or roll[2] == 7:
        peniaze += 1
    else:
        print("Nayy")
    
peniaze = 100
button1 = tk.Button(text="Start",
                    command=Start,
                    width=15,
                    height=3)
button1.pack()
