import random

def valitse_vaikeusaste():
    while True:
        vaikeusaste = input("Anna vaikeusaste (1/2/3): ")
        if vaikeusaste in ['1', '2', '3']:
            return int(vaikeusaste)
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

def generoi_luvut(vaikeusaste):
    if vaikeusaste == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif vaikeusaste == 2:
        return random.randint(10, 19), random.randint(10, 19)
    elif vaikeusaste == 3:
        return random.randint(20, 99), random.randint(20, 99)

try:
    while True:
        vaikeusaste = valitse_vaikeusaste()
        while True:
            luku1, luku2 = generoi_luvut(vaikeusaste)
            vastaus = input(f"{luku1} x {luku2} = ")
            if vastaus.lower() == 'ctrl-c':
                break
            elif int(vastaus) == luku1 * luku2:
                print("oikein!")
            else:
                print("väärin!")
except KeyboardInterrupt:
        print("\nOhjelma keskeytetty.")
        
        
      
   



    
            
            
















    