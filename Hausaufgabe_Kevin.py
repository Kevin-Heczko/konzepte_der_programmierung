#Aufgabe 1a)
import math

#toBin(zahl: int): int
#Precondition: None
#Postcondition:
#   Effect: Umwandlung der Zahl von dezimal zu Binär
#   Ergebnis: None
def toBin(zahl):
    binaer = ""
    for _ in range(int(math.log(zahl, 2)) + 1):
        binaer = str(zahl % 2) + binaer
        zahl //= 2
    print(binaer)

def toBin_1(zahl):
    binaer_1 = ""
    while zahl > 0:
        binaer_1 = str(zahl % 2) + binaer_1
        zahl //= 2
    print(binaer_1)

def toBin_2(zahl):
    if zahl == 0:
        return ""
    else:
        return toBin_2(zahl//2) + str(zahl % 2)


#toBin(5000)
#toBin_1(5000)
#print(toBin_2(5000))

#Aufgabe 1b)
#oddsum(n: int): int
#Precondition: None
#Postcondition:
#   Effect:
#   result:
def oddsum(n):
    summe = 0
    for a in range(n):
        if a % 2 == 0:
            continue
        else:
            summe += a
    return summe
#print(oddsum(10))

def oddsum_1(n):
    summe_1 = 0
    mitzaehlen = 0
    while summe_1 == 0 or mitzaehlen // n != 1:
        mitzaehlen += 1
        if mitzaehlen % 2 == 0:
            continue
        else:
            summe_1 += mitzaehlen
    return summe_1
#print(oddsum_1(10))

def oddsum_2(n):
    if n == 0:
        return 0
    else:
        return oddsum_2(n-1) + n * (n % 2)
#print(oddsum_2(10))

#Aufgabe c)
#plattmachen(liste: list): list
#Precondition: None
#Postcondition:
def plattmachen(liste):
    for i in liste:
        liste.append(1)
    return liste
liste_1 = [[1, 2, 3, 4], [1, 2, 3, 4]]
print(plattmachen(liste_1))
C:\Users\heczk\konzepte_der_programmierung\Hausaufgabe_Kevin.py