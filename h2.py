def Reverse(pole):
    r = []
    for i in range(len(pole)):
        prvok = pole[len(pole) - (i+1)]
        r.append(prvok)
    print(r)

def Reverse2(pole):
    r = []
    for i in range(len(pole)-1, -1, -1):
        prvok = pole[i]
        r.append(prvok)
    print(r)

##Reverse([1,2,3,4])
##Reverse2([1,2,3])
##
##pole = [1,2,3,4]
##pole.pop()
##print(pole)

pole1 = [1,2,3,4,5]
pole2 = [1,2,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,4,5,1]

def is_duplicate(pole):
    for i in range(len(pole)):
        for j in range(i+1, len(pole)):
            if pole[i] == pole[j]:
                print(pole[i])
                return True
    return False

print(is_duplicate(pole1))
print(is_duplicate(pole2))
print(is_duplicate([1,57,34,3,468,34,4,384,348,433,7,384,84,34,384,483,43,4,8,684,384,34,48,38]))



###############################
#### PREBRAT RANGE ############
###############################









