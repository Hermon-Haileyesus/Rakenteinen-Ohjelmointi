import random
import datetime

# Tiedoston nimi
file_name = "nimet.txt"

def satunnainen_rivi():
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def ika_kysely():
    nykyinen_vuosi = datetime.datetime.now().year
    taysi_ikaiset = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            nimi, vuosi = line.split()
            if nykyinen_vuosi - int(vuosi) >= 18:
                taysi_ikaiset.append(line.strip())
    return taysi_ikaiset

def poiminta():
    n = int(input("Anna luku: "))
    print(f"Joka, {n}.rivi :")
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        poiminnat = [f"{i+1}: {line.strip()}" for i, line in enumerate(lines) if (i+1) % n == 0]
    return poiminnat 
def nimikysely():
    nimi = input("Anna nimi: ").strip()
    nykyinen_vuosi = datetime.datetime.now().year
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            nimi_tiedostossa, vuosi = line.split()
            if nimi_tiedostossa.lower() == nimi.lower():
                ika = nykyinen_vuosi - int(vuosi)
                return f"{nimi_tiedostossa} on {ika}v."
    return "Nimeä ei löydy!"

def main():
    while True:
        valinta = input("(s)atunnainen rivi, (i)käkysely vai (p)oiminta vai (n)imikysely? ").strip().lower()
        if valinta == 's':
            print(satunnainen_rivi())
        elif valinta == 'i':
            taysi_ikaiset = ika_kysely()
            print("Tänä vuonna täysi-ikäiset: ")
            for rivi in taysi_ikaiset:
                print(rivi)
        elif valinta == 'p':
            poiminnat = poiminta()
            for rivi in poiminnat:
                print(rivi)
        elif valinta == 'n':
            print(nimikysely())
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

if __name__ == "__main__":
    main()
