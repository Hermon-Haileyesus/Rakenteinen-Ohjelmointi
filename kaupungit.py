import random
# vaihe 1
with open ("pkaupungit.txt", encoding="UTF-8") as f:
    rivit = f.readlines()
for rivi in rivit:
    rivi = rivi. strip()  
    print(rivi)
#vaihe 2
for rivi in rivit:
    rivi = rivi.strip()
    rivi_osa =rivi.split("?")
    print(rivi_osa[0])
    print(rivi_osa[1])
#vaihe 3
oikeinlkm = 0
for rivi in rivit:
    rivi = rivi.strip()
    rivi_osa =rivi.split("?")
    maa = rivi_osa[0]
    pkaupunki = rivi_osa[1]
    vastaus = input(f"Maan nimi on {maa}. Anna pääkaupunki (quit = lopetus): ")
    if vastaus.lower() == "quit":
        break
    elif vastaus.lower() == pkaupunki.lower():
        print("oikein")
        oikeinlkm +=1
    else:
        print(f"väärin, oikea vastaus:{pkaupunki}")
print(f"oikein vastattuja kysymyksiä: {oikeinlkm}")
#vaihe 4
with open ("pkaupungit.txt", encoding="UTF-8") as f:
    rivit = f.readlines()
random.shuffle(rivit)

kysymykset = 0
oikeinlkm = 0
for rivi in rivit:
    rivi = rivi.strip()
    rivi_osa =rivi.split("?")
    maa = rivi_osa[0]
    pkaupunki = rivi_osa[1]
    vastaus = input(f"Maan nimi on {maa}. Anna pääkaupunki (quit = lopetus): ")

    if vastaus.lower() == "quit".lower():
        break
    kysymykset +=1
    if vastaus.lower() == pkaupunki.lower():
        print("oikein")
        oikeinlkm +=1
    else:
        print(f"väärin, oikea vastaus:{pkaupunki}")
if kysymykset > 0:
    onnistumisprosentti = (oikeinlkm /kysymykset) * 100
    print(f"Oikeiden vastausten lukumäärä: {oikeinlkm}")
    print(f"Onnistumisprosentti: {onnistumisprosentti:.2f}%")
else:
    print("Ei yhtään kysymystä vastattu.")




    
    
    
