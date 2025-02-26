import random
with open('sanat.txt', 'r') as file:
    sanat = file.readlines()
def käyttäjän_vastaus():
       while True:
            vastaus = int(input("Montako kierrosta mennään? "))
            if vastaus >= 1:
               return vastaus
while True:
    
    luku = käyttäjän_vastaus()
    
    for kierros in range(1, luku + 1):
        sana1 = random.choice(sanat).strip()
        sana2 = random.choice(sanat).strip()
        if kierros % 3 == 0:
            print(sana1)
        elif kierros % 5 == 0:
            print(sana2)
        elif kierros % 3 == 0 and kierros % 5 == 0:
             print(f"{sana1}{sana2}")
        else:
            print(kierros)
