with open('luvut.txt', encoding='utf-8') as f:

     rivit = f.readlines()

lkm = 0

pienin = 500

# Poistetaan rivinvaihtomerkit

for rivi in rivit:

    lkm += 1

    print("rivi{} : {}".format(lkm, rivi.strip()))

    luku = int(rivi)

    if luku < pienin:

             pienin = luku

print(pienin)