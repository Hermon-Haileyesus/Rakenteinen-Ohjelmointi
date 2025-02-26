import random
with open('sanat.txt', 'r') as file:
    sanat = [line.strip() for line in file]
print(sanat)
while True:
    # Käytä yllä olevia osia täällä kutsumalla ne uudelleen tarpeen mukaan
    # Tässä esimerkissä toistan yllä olevan prosessin
    while True:
        try:
            luku = int(input("Montako kierrosta mennään? "))
            if luku >= 1:
                break
            else:
                print("Annetun luvun tulee olla vähintään 1.")
        except ValueError:
            print("Syötä kokonaisluku.")
    
    for kierros in range(1, luku + 1):
        sana1, sana2 = random.choice(sanat), random.choice(sanat)
        if kierros % 3 == 0 and kierros % 5 == 0:
            print(f"{sana1}{sana2}")
        elif kierros % 3 == 0:
            print(sana1)
        elif kierros % 5 == 0:
            print(sana2)
        else:
            print(kierros)