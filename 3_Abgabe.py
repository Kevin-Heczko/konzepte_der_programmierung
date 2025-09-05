#countAsTroll(zahl: int): string
#Precondition: Nonee
#Postcondition:
#   effect: None
#   result: Zahl im Format de Trolls
def countAsTroll(zahl: int):
    zuordnung: {
        0: "",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "MANY",
        16: "LOTS"
    }
    if zahl in range(0,4):
        return zuordnung.get(zahl)
print(countAsTroll(3))

#zahl 1-3 ANKER
#zahl größer 16 schritt