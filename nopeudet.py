with open('nopeudet.txt', encoding='utf-8') as f:

     rivit = f.readlines()
lkm = 0
pienin = 250
suurin = 0
yhteis_nopeus = 0
for rivi in rivit:

    lkm += 1
    
    print("{} : {}".format(lkm, rivi.strip()))

    nopeus= int(rivi)
    yhteis_nopeus += nopeus
    if nopeus < pienin:
          pienin = nopeus
    if nopeus > suurin:
         suurin = nopeus
keskiarvo = yhteis_nopeus / lkm
print(f"Kaikkiaan {lkm} nopeutta")
print(f"Alhaisin ajonopeus {pienin} km/h")
print(f"Suurin ajonopeus {suurin} km/h")
print(f"Ajonopeuksien keskiarvo: {keskiarvo:.2f} km/h")