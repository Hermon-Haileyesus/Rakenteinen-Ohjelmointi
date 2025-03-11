import random
from datetime import datetime
#vaihe1
with open("nimet.txt","r",encoding="UTF-8") as file:
    rivit = file.read().splitlines()
print( random.choice(rivit))

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
   
      
      




while True:
       valinta = input("(s)atunnainen rivi, (i)käkysely, (p)oiminta vai (n)imikysely?")
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
             print(nimikysely(rivit))
             
             


       else:
              print("Virheellinen valinta. Yritä uudelleen")


              