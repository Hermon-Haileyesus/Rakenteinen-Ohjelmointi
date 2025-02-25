with open("artikkeli.txt", "r" , encoding ="UTF-8") as f:
    rivit = f.read()
sana = input("Anna etsittävä sana: ")
lasku = rivit.count(sana)
if lasku > 0:
    print(f"Sana {sana} esiintyi tekstissä {lasku} kertaa")
else:
    print(f"Sanaa {sana} ei löytynyt!")


#vaihe 2

with open("artikkeli.txt", "r" , encoding ="UTF-8") as f:
    rivit = f.read()
sana = input("Anna etsittävä sana: ")
lasku = rivit.count(sana)
paikka = rivit.find(sana)
if paikka != -1:
        jäljellä = len(rivit) - paikka
        print(f"Sana esiintyy tiedostossa kohdassa {paikka}. Siitä eteenpäin on jäljellä {jäljellä} merkkiä.")
else:
    print(f"Sanaa {sana} ei löytynyt!")
#vaihe 3
with open("artikkeli.txt", "r" , encoding ="UTF-8") as f:
    rivit = f.read()
sana = input("Anna etsittävä sana: ")
lasku = rivit.count(sana)
nykyinen_paikka = 0
while True:
        paikka = rivit.find(sana,nykyinen_paikka)

        if paikka == -1:
           break
        jäljellä = len(rivit) - paikka
        print(f"Sana esiintyy tiedostossa kohdassa {paikka}. Siitä eteenpäin on jäljellä {jäljellä} merkkiä.")
        nykyinen_paikka = paikka + 1

#vaihe 4
with open("artikkeli.txt", "r" , encoding ="UTF-8") as f:
    rivit = f.read()
sana = input("Anna etsittävä sana: ")
lasku = rivit.count(sana)
rivi = rivit.split('\n')
nykyinen_paikka= 0
while True:
        paikka = rivit.find(sana, nykyinen_paikka)

        if paikka == -1:
           break
        rivi_luku =rivit.count('\n',0, paikka) + 1
        rivin_paikka = paikka - rivit.rfind('\n',0 ,paikka) - 1 
        jäljellä = len(rivit) - paikka
        print(f"Sana esiintyy tiedostossa kohdassa {paikka}, rivillä {rivi_luku}, kohdassa {rivin_paikka}. Siitä eteenpäin on jäljellä {jäljellä} merkkiä.")
        nykyinen_paikka = paikka + 1

#vaihe 5
with open("artikkeli.txt", "r" , encoding ="UTF-8") as f:
    rivit = f.read()
sana = input("Anna etsittävä sana: ")
lasku = rivit.count(sana)
rivi = rivit.split('\n')
nykyinen_paikka= 0
while True:
        paikka = rivit.find(sana, nykyinen_paikka)

        if paikka == -1:
           break
        lause_alku = rivit.rfind('.',0, paikka)+ 1
        lause_loppu = rivit.find('.',paikka) + 1
        if lause_loppu == -1:
             lause_loppu = len(rivit)
        lause = rivit[lause_alku:lause_loppu].strip()
        jäljellä = len(rivit) - paikka
        rivi_luku =rivit.count('\n',0, paikka) + 1
        rivin_paikka = paikka - rivit.rfind('\n',0 ,paikka) - 1 
        print(f"Sana esiintyy tiedostossa kohdassa {paikka}, rivillä {rivi_luku}, kohdassa {rivin_paikka}.")
        print(f"Siitä eteenpäin on jäljellä {jäljellä} merkkiä. Lause: '{lause}'")
        nykyinen_paikka = paikka + 1
