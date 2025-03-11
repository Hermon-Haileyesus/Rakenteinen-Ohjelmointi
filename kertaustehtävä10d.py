import random
from datetime import datetime
tänä_vuona = datetime.now().year
#vaihe1
with open("nimet.txt","r",encoding="UTF-8") as file:
    rivit = file.read().splitlines()
print( random.choice(rivit))
nimet = {}
for rivi in rivit:
      nimi , vuosi = rivi.split()
      nimet[nimi] = vuosi

#Vaihe2
def ikä_kysely(rivit):
     tänä_vuona = datetime.now().year
     täysi_ikäiset = []
     for rivi in rivit:
            if (tänä_vuona - int(rivi.split()[1])) >= 18:
                   täysi_ikäiset.append(rivi)
     return täysi_ikäiset
#vaihe3
def poiminta(rivit):
       poiminnat = []
       for i, rivi in enumerate(rivit,1):
            poiminnat.append( f"{i}: {rivi.strip()}")
            i=+1
       return poiminnat
#vaihe4
def nimikysely(rivit):
   while True:
      nimi = input("Anna nimi: ").strip()
      tänä_vuona = datetime.now().year
      
      for rivi in rivit:       
         oikea_nimi , vuosi = rivi.split()
         if nimi.lower() == oikea_nimi.lower():
              ikä = tänä_vuona - int(vuosi)
              return f"{oikea_nimi} on {ikä}v."
       
      print("Nimeä ei löydy!")
#vaihe5
def kaikki_nimet():
      iät=[]
      tänä_vuona = datetime.now().year
      for rivi in rivit:
            print(f"{rivi} v")
            iät.append(tänä_vuona - int(rivi.split()[1]))
      keskiarvo = sum(iät) / len(iät)
      print(f"Ikien keskiarvo: {keskiarvo:.1f}")
      print()
def osa_nimet():
      määrät = int(määrä) + 1 
      iät = []
        
      for i in range(1,määrät):
           while True:
              nimi= input(f"Syötä nimi {i}: ").strip().capitalize()
              if nimi in nimet:
                   ikä = tänä_vuona - int(nimet[nimi])  # Oletetaan, että vuodet ovat syntymävuosia
                   print(f"{nimi} on {ikä}v")
                   iät.append(ikä)
                   break
              
              else:
               print("Nimeä ei löytynyt!")
               
      keskiarvo = sum(iät) / len(iät)
      print(f"Ikien keskiarvo:  {keskiarvo:.1f}")     
 #vaihe 6           
def kirjaimet():
      kirjain = input("Anna kirjain: ").strip().lower()
      iät = []
      for nimi in nimet:
         if kirjain in nimi.lower():
                    ikä = tänä_vuona -int( nimet[nimi])
                    print(f"{nimi} on {ikä}v")
                    iät.append(ikä)
            
      if iät:
                keskiarvo = sum(iät) / len(iät)
                print(f"Keskimääräinen ikä: {keskiarvo:.1f}")            
      else:
                print("Yhtään nimeä ei löytynyt annetulla kirjaimella.")
#vaihe 7
              
def kirjaimet_kysely():   
   kirjaimet = []
   while True:
      vastaus = input("Anna kirjain tai 'hae': ").strip().lower()
      if vastaus == "hae":
            break
      kirjaimet.append(vastaus)
   
   tyyppi = input("Etsitäänkö nimet, joissa on (k)aikki kirjaimet, (j)oku kirjaimista vai (e)i mikään kirjaimista? ")
   iät =[]
   for nimi in nimet:
                nimi_pienella = nimi.lower()
                if(tyyppi == "k" and all(k in nimi_pienella for k in kirjaimet)) or \
                  (tyyppi == "j" and any(k in nimi_pienella for k in kirjaimet)) or \
                   (tyyppi == "e" and not any(k in nimi_pienella for k in kirjaimet)):
                    ikä = tänä_vuona - int( nimet[nimi])
                    print(f"{nimi} on {ikä}v")
                    iät.append(ikä)
   if iät:
      ikien_keskiarvo = sum(iät) / len(iät)
      print(f"Keskimääräinen ikä: {ikien_keskiarvo:.1f}")
   else:
      print("Yhtään nimeä ei löytynyt annetuilla kirjaimilla.")
  
    
      
      


try:

 while True:
       valinta = input("(s)atunnainen rivi, (i)käkysely, (p)oiminta, (n)imikysely vai (k)irjainkysely?")
       if valinta.strip().lower() == "s":
              print(random.choice(rivit))
       elif valinta.strip().lower() == "i":
              täysi_ikäiset = ikä_kysely(rivit)
              print("Tänä vuonna täysi-ikäiset: ")
              for rivi in täysi_ikäiset:
                     print(rivi)
       elif valinta.strip().lower() == "p":
             luku =  int(input("Anna luku: "))
             print(f"Joka {luku}. rivi")
             poiminnat= poiminta(rivit)
             for rivi in poiminnat:
                   if int(rivi.split(':')[0]) % luku == 0:
                         print(rivi)
       elif valinta.strip().lower() == "n": 
               määrä = input("Kuinka monta nimeä haluat käsitellä? ").strip().lower()
               if määrä == "kaikki":
                     kaikki_nimet()
               else:
                     osa_nimet()
       elif valinta.strip().lower() == "k":
             kirjaimet_kysely()
             
       else:
              print("Virheellinen valinta. Yritä uudelleen")
except KeyboardInterrupt:
      print("\n ohjelma on loppunut!Moikka")
