import random

def heita_noppaa():
    sivut = int(input("Montako sivua nopassa? "))
    tulos = random.randint(1, sivut)
    print(f"Nopasta tuli {tulos}")
        

def kivi_paperi_sakset():
    valinta = random.choice(["K", "P", "S"])
    print(f"Valitsen {valinta}")

def lottorivi():
    rivinumerot = random.sample(range(1, 41), 7)
    print(f"Rivisi on {rivinumerot}")
print("Mahdolliset toiminnot ovat:")
print("1 - heitä noppaa")
print("2 - kivi, paperi tai sakset")
print("3 - lottorivi")

while True:
        try:
            valinta = input("Mitä tehdään (1-3)? ")
            if valinta.lower() =="ctrl-c":
                print("\n Peli on lopenut")
                break

            if int(valinta ) == 1:
                heita_noppaa()
            elif int(valinta ) == 2:
                kivi_paperi_sakset()
            elif int(valinta ) == 3:
                lottorivi()
            else:
                print("En ymmärrä, valitse uudestaan...")
        except KeyboardInterrupt:
            print("\nOhjelma lopetettu.")
            break
