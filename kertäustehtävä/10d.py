import random
from datetime import datetime
tänä_vuona = datetime.now().year
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
            nimi= input(f"Syötä nimi {i}: ").lower()
            for rivi in rivit:
                        oikea_nimi , vuosi = rivi.split()
                        if nimi == oikea_nimi.lower():
                              ikä = tänä_vuona - int(vuosi)
                              print(f"{nimi} on {ikä} v.")
                              iät.append(ikä)
                              break
                        else:
                              print("Nimeä ei löytynyt!")
                              break

      keskiarvo = sum(iät) / len(iät)
      print(f"Ikien keskiarvo:  {keskiarvo:.1f}")     
            
                        
            
            

   
      
      




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
               määrä = input("Kuinka monta nimeä haluat käsitellä? ").strip().lower()
               if määrä == "kaikki":
                     kaikki_nimet()
               else:
                     osa_nimet()
              
             
             


       else:
              print("Virheellinen valinta. Yritä uudelleen")
