def laskuri(määrä, hinta):
    return määrä * hinta

määrä = float(input("Anna tuotteen määrä: "))
hinta = float(input("Anna tuotteen hinta: "))
summa = laskuri(määrä, hinta)
print(f"Tuotteen kokonaishinta on : {summa:.2f} euroa")


