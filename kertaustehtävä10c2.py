import random

def lue_loukkaukset(tiedostonimi):
    loukkaukset = []
    with open(tiedostonimi, 'r') as tiedosto:
        for rivi in tiedosto:
            loukkaus, vastaus = rivi.strip().split(':')
            loukkaukset.append((loukkaus, vastaus))
    return loukkaukset
def peli():
    loukkaukset = lue_loukkaukset('insults.txt')
    voitot = 0
    for i in range(3):
        loukkaus, oikea_vastaus = random.choice(loukkaukset)
        vastaukset = [oikea_vastaus] + random.sample([v[1] for v in loukkaukset if v[1] != oikea_vastaus], 2)
        random.shuffle(vastaukset)
        print(f'Your opponent says: "{loukkaus}"\n')
        for i, vastaus in enumerate(vastaukset, 1):
            print(f'{i}. {vastaus}')
        valinta = int(input('\nHow do you respond? '))
        if vastaukset[valinta - 1] == oikea_vastaus:
            print('You win this time!\n')
            voitot += 1
        else:
            print('Ha! You lose!\n')
    if voitot >= 2:
        print('You won the duel!')
    else:
        print('You lost the duel!')

if __name__ == "__main__":
    peli()





