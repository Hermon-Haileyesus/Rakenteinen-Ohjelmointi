import random


def lisää_sanapari(tiedosto, suomi, ruotsi):
    with open(tiedosto, 'a', encoding='utf-8') as f:
        f.write(f'\n{suomi}={ruotsi}')

def lue_sanakirja(tiedosto):
    sanakirja = {}
    with open(tiedosto, 'r', encoding='utf-8') as f:
        for rivi in f:
            suomi, ruotsi = rivi.strip().split('=')
            sanakirja[suomi] = ruotsi
    return sanakirja


def kysely(sanakirja):
    pisteet = 0
    kysytyt = 0
    while True:
        suomi, ruotsi =  random.choice(list(sanakirja.items()))
        if random.choice([True, False]):
            vastaus = input(f'Mitä "{suomi}" on ruotsiksi? ')
            oikea_vastaus = ruotsi
        else:
            vastaus = input(f'Mitä "{ruotsi}" on suomeksi? ')
            oikea_vastaus = suomi
        
        if vastaus.lower() == 'quit':
            print(f'Kiitos! Sait {pisteet} pistettä {kysytyt} sanasta.')
            if kysytyt > 0:
                prosentit = (pisteet / kysytyt) * 100
                if prosentit > 85:
                    print('Hieno suoritus!')
                elif prosentit < 50:
                    print('Nyt meni aika heikosti!')
            break
        elif vastaus.lower() == 'lisää':
            uusi_suomi = input("Anna uusi suomenkielinen sana: ")
            uusi_ruotsi = input("Anna uusi ruotsinkielinen sana: ")
            lisää_sanapari(tiedostonimi, uusi_suomi, uusi_ruotsi)
            sanakirja = lue_sanakirja(tiedostonimi)  
            print(f'Uusi sanapari "{uusi_suomi}={uusi_ruotsi}" lisätty.')
            continue
        
        kysytyt += 1
        
        if vastaus.lower() == oikea_vastaus.lower():
            pisteet += 1
            print('Loistavaa, oikein meni!')
        else:
            print(f'Nyt meni pieleen, oikea vastaus oli "{oikea_vastaus}".')
        
        print(f'Pisteesi nyt: {pisteet}/{kysytyt}')

tiedostonimi ="sanaparit4.txt"
sanakirja = lue_sanakirja(tiedostonimi)
kysely(sanakirja)
