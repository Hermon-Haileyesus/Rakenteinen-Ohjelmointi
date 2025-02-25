while True:
    mitta = input("Anna mitta: ")
    numero = float (mitta.split()[0])
    yksikkö = mitta.split()[1].lower()
    tuuma = yksikkö.find("tuumaa")
    sentti = yksikkö.find("cm")
    kilo = yksikkö.find("kg")
    pauna =yksikkö.find("paunaa")
    jalka = yksikkö.find("jalkaa")
    metri = yksikkö.find("metriä")
    litra = yksikkö.find("litraa")
    tuoppi = yksikkö.find("tuoppia")
    
    if tuuma!= -1 :
        print(f"{mitta} on {numero * 2.54} cm ")
    elif sentti != -1:
        print(f"{mitta} on {numero /2.54} tuumaa")
    elif kilo != -1:
         print(f"{mitta} on {numero *2.20462} paunaa")
    elif pauna != -1:
         print(f"{mitta} on {numero /2.20462} kg")
    elif jalka != -1:
         print(f"{mitta} on {numero *0.3048} m")
    elif metri != -1:
         print(f"{mitta} on {numero/ 0.3048} jalkaa")
    elif litra != -1:
         print(f"{mitta} on {numero *2.11338} tuoppeja")
    elif tuoppi != -1:
         print(f"{mitta} on {numero /2.11338} litraa")
    else:
        print("En tunne tuota yksikköä!")
        break