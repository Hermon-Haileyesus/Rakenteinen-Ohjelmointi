with open('kuukaudet.txt', encoding='utf-8') as f:
    # Luetaan tiedoston rivit muuttujaan data.
    # Näin luettua dataa voimme käsitellä rivi kerrallaan.
    data = f.readlines()
# Käsitellään tiedoston sisältöä rivi kerrallaan for-lauseen avulla.
print(data)
for rivi in data:

    # Poistetaan rivin lopusta rivinvaihto.
    # strip() poistaa kaikki tulostumattomat merkit merkkijonon alusta JA lopusta.
    # Tulostumattomia merkkejä ovat esim. välilyönti, sarkain ja rivinvaihto.

    rivi = rivi.strip()

    # Tulostetaan rivi kirjoittaen sen loppuun kaksoispiste ja välilyönti, ei rivinvaihtoa.

    print(rivi, end=': ')

    if rivi =='Tammikuu' or rivi =='Helmikuu' or rivi =='Joulukuu':
        print('Tervetuloa kylmimpään vuodenaikaan')
    elif rivi =='Maaliskuu' or rivi=='Huhtikuu' or rivi== 'Toukokuu':
        print('Kevät on täällä')
    elif rivi == 'Kesäkuu' or rivi == 'Heinäkuu' or rivi=='Elokuu':
        print('Tervetuloa aurinkoiseen kesään')
    else:
        print('Syksy on ihanaa')
    
