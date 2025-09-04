#Aufgabe 1a)
import math

#toBin(zahl: int): int
#Precondition: None
#Postcondition:
#   Effect: Umwandlung der Zahl von dezimal zu Binär
#   Ergebnis: None
def toBin(zahl):
    binär = ""
    for i in range(int(math.log(zahl, 2))+1):
        binär = str(zahl % 2) + binär
        zahl //= 2
    print(binär)

def toBin_1(zahl):
    binär_1 = ""
    while zahl > 0:
        binär_1 = str(zahl % 2) + binär_1
        zahl //= 2
    print(binär_1)

def toBin_2(zahl):
    if zahl == 0:
        return ""
    else:
        return toBin_2(zahl//2) + str(zahl % 2)


toBin(5000)
toBin_1(5000)
print(toBin_2(5000))

#Aufgabe 1b)
