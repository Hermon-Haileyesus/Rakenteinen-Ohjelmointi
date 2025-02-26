import random
with open("insults.txt","r", encoding="UTF-8",) as f:
        rivit = f.readlines()
random.shuffle(rivit) 
loukkaukset_vastaukset = []
vastaukset = []
for rivi in rivit:
    loukkaus, oikea_vastaus = rivi.strip().split(':')
    vastaukset.append(oikea_vastaus)
    loukkaukset_vastaukset.append((loukkaus,oikea_vastaus ))
    
def peli():
    
    voitot = 0
    for i in range(3):
        loukkaus,oikea_vastaus = random.choice(loukkaukset_vastaukset)
        print(f'Your opponent says: "{loukkaus}"\n')
        vaihtoehto = [oikea_vastaus]
        while len(vaihtoehto) < 3:
            väärä_vastaus = random.choice(vastaukset)
            if väärä_vastaus  != oikea_vastaus:
                vaihtoehto.append(väärä_vastaus)
        random.shuffle(vaihtoehto)
        for i, vastaus in enumerate(vaihtoehto, 1):
            print(f'{i}. {vastaus}')
        valinta = int(input('\nHow do you respond? '))
        if vaihtoehto[valinta - 1] == oikea_vastaus:
            print('You win this time!\n')
            voitot += 1
        else:
            print('Ha! You lose!\n')
    if voitot >= 2:
        print('You won the duel!')
    else:
        print('You lost the duel!')

peli()

              

