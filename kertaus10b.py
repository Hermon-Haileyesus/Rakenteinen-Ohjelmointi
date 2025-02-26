import random
print("Hei, tervetuloa numeronarvauspeliin!")
print("Tehtäväsi on arvata numero väliltä 0 - 100.\n")
while True: 
    try:
      oikea_luku = random.randint(0, 100)
      arvauksia = 0
      while True:
         try:
           arvaus = int(input("Anna arvauksesi: "))
           arvauksia += 1
                
           if arvaus < oikea_luku:
             print("Arvattava numero on suurempi!\n")
           elif arvaus > oikea_luku:
             print("Arvattava numero on pienempi!\n")
           else:
             print(f"Arvasit oikein! Sinulla meni {arvauksia} arvausta!\n")
             break
         except ValueError:
            print("syötä kokonais luku")
      print("Tehtäväsi on arvata numero väliltä 0 - 100")
    except KeyboardInterrupt:
       break
        
 
        

