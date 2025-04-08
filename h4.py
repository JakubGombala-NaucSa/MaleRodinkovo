from random import randint

##pole = []
##
##for i in range(10):
##    pole.append(randint(1,50))
##
##print(pole)
##
##print("mensie", end=": ")
##for cislo in pole:
##    if cislo < 15:
##        print(cislo, end=", ")
##
##print()
##print("vacsie", end=": ")
##for cislo in pole:
##    if cislo > 15:
##        print(cislo, end=", ")


vysledok = []
print("|", end="")
for i in range(3):
    cislo = randint(1,10)
    vysledok.append(cislo)
    print(cislo, end="|")

##vysledok = [7,7,7]

if (vysledok[0] == 7 and
    vysledok[1] == 7 and
    vysledok[2] == 7):
    print("\nyayyy")

##for cislo2 in vysledok:
##    if cislo2 == 7:
##    print("nieco")
##
##


















