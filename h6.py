import tkinter as tk

platno = tk.Canvas(bg="white", width=500, height=500)
platno.pack()

platno.create_oval(200,200,300,300, fill="lime")

# ------------PREMENNE------------
body = 0
bodov_za_klik = 1
bodov_za_sekundu = 0
cena_1 = 25
cena_2 = 100
# --------------------------------

platno.create_text(20,10, text = "Body: ")
platno.create_text(60,10, text = str(body), tag="body")

def uprav_body():
    global body, bodov_za_sekundu
    platno.delete("body")
    platno.delete("bzs")
    platno.create_text(60,10, text = str(body), tag="body")
    platno.create_text(440,10, text= str(bodov_za_sekundu), tag="bzs")

def klik_lave(event):
    global body, bodov_za_klik
    body += bodov_za_klik
    uprav_body()

def plus_klik():
    global body, bodov_za_klik, cena_1
    if body >= cena_1:
        vyhodnotenie(True, 0)
        bodov_za_klik += 1
        body -= cena_1
        cena_1 *= 2
        uprav_body()
    else:
        vyhodnotenie(False, cena_1-body)

def vyhodnotenie(pravda, rozdiel):
    platno.delete("vylepsenie")
    if pravda:
        platno.create_text(250, 400, text="kupil si si vylepsenie", tag="vylepsenie")
    else:
        platno.create_text(250, 400, text="do vylepsenia ti chýba: " + str(rozdiel), tag="vylepsenie")

def plus_jedna():
    global body, cena_2, bodov_za_sekundu
    if body >= cena_2:
        vyhodnotenie(True, 0)
        bodov_za_sekundu += 1
        body -= cena_2
        cena_2 *= 2
        uprav_body()
    else:
        vyhodnotenie(False, cena_2-body)

def my_loop():
    global body, bodov_za_sekundu
    body += bodov_za_sekundu/10
    body = round(body, 1)
    uloz()
    uprav_body()
    platno.after(100, my_loop)

def uloz():
    subor = open("save.txt", "w")

    subor.write(str(body) + "\n")
    subor.write(str(bodov_za_klik) + "\n")
    subor.write(str(bodov_za_sekundu) + "\n")
    subor.write(str(cena_1) + "\n")
    subor.write(str(cena_2) + "\n")

    subor.close()

def nacitaj():
    global body, bodov_za_sekundu, bodov_za_klik, cena_1, cena_2
    try:
        subor = open("save.txt", "r")
        premenne = []
        for riadok in subor:
            premenne.append(float(riadok[:len(riadok)-1]))
        
        body = premenne[0]
        bodov_za_klik = premenne[1]
        bodov_za_sekundu = premenne[2]
        cena_1 = premenne[3]
        cena_2 = premenne[4]
    except:
        print("a")
        

nacitaj()
my_loop()
platno.bind("<Button-1>", klik_lave)


B_PlusJedna = tk.Button(text="Plus Klik", command=plus_klik, width=15, height=3)
B_PlusJedna.pack()

B_PlusJednaZaSekundu = tk.Button(text="Plus 1 za s", command=plus_jedna, width=15, height=3)
B_PlusJednaZaSekundu.pack()
