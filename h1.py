cisla = [1,2,7,2,5,3,15,13512,183,135]
print(cisla)
print(cisla[0])
print(cisla[2])
print(len(cisla))

cisla[4] = 25
print(cisla[4]+20)
print(cisla)
    
for i in range(len(cisla)):
    if cisla[i] < 17:
        cisla[i] += 5
    else:
        cisla[i] -= 5

print(cisla)

for i in cisla:
    print(i)


text = "Ahojky ako sa dnes mas ?"
sifra = "Ashcovjbknym lakkjoh gstay udinoeps[ lmkajsh g?f"
print(len(text))
print(text)
print(text[0:4])
print(text[:4])
print(text[4:len(text)])
print(text[4:])

print(sifra)
print(sifra[::2])

from random import randint

def VytvorSifru(text, krok):
    sifra = ""
    for i in text:
        sifra += i
        for j in range(krok):
            sifra += chr(randint(97,122))
        
    return sifra

textNaSifru= "Toto je moje najvacsie tajomstvo"
novaSifra = VytvorSifru(textNaSifru,107)
print("Sifra:")
print(novaSifra)
print("Desifra:")
print(novaSifra[::108])










