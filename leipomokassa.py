#vaihe 1
def laskuri(tuote, määrä):
    hinnat = {
        "voipulla": 0.5,
        "munkkirinkilä": 0.8,
        "possumunkki": 1.0,
        "piispanmunkki": 1.2
    }
    
    if tuote in hinnat:
        return määrä * hinnat[tuote]
    else:
        return 0
#vaihe 2
tuote = input("Mitä tuotetta haluaa ostaa (voipulla, munkkirinkilä, possumunkki, piispanmunkki)? ").strip().lower()
määrä = int(input("Anna tuotteen määrä: "))
summa = laskuri(tuote, määrä)
print(f"Tuotteen kokonaishinta on: {summa:.2f} euroa")
#vaihe 3
summa = 0
while True:
    tuote = input("Mitä tuotetta halua ostaa (voipulla, munkkirinkilä, possumunkki, piispanmunkki ,'lopeta' = quit)? ").strip().lower()
    if tuote =="lopeta":
        break
    määrä = int(input("Anna tuotteen määrä: "))
    summa += laskuri(tuote, määrä)
print(f"Tuotteen kokonaishinta on: {summa:.2f} euroa")