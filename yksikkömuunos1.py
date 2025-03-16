
while True: 
 
    user_input = input("Anna mitta : ")
    try:
        
        split_index = user_input.find(" ")
        amount = float(user_input[:split_index])  
        unit = user_input[split_index + 1:].strip().lower()

       
        if unit in ["tuumaa", "in"]:
            print(f"{amount} tuumaa on {amount * 2.54:.2f} cm")
        elif unit in ["senttiä", "cm"]:
            print(f"{amount} cm on {amount / 2.54:.2f} tuumaa")
        elif unit in ["jalkaa", "ft"]:
            print(f"{amount} jalkaa on {amount * 0.3048:.2f} metriä")
        elif unit in ["metriä", "m"]:
            print(f"{amount} m on {amount / 0.3048:.2f} jalkaa")
        elif unit in ["kiloa", "kg"]:
            print(f"{amount} kg on {amount * 2.20462:.2f} paunaa")
        elif unit in ["paunaa", "lb", "lbs"]:
            print(f"{amount} paunaa on {amount / 2.20462:.2f} kiloa")
        elif unit in ["litraa", "l"]:
            print(f"{amount} litraa on {amount * 2.11338:.2f} tuoppia")
        elif unit in ["tuoppia", "pint"]:
            print(f"{amount} tuoppia on {amount / 2.11338:.2f} litraa")
        else:
            print("En tunne tuota yksikköä!")
            break
    except ValueError:
        print("Tarkista syöte! Anna se muodossa 'määrä yksikkö' (esim. '10 kg').")

