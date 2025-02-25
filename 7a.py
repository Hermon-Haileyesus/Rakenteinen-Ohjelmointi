nimi1 = input("Anna ensimmäinen nimi: ")
nimi2 = input("Anna toinen nimi: ")
nimi3 = input("Anna kolmas nimi: ")
nimi4 = input("Anna neljäs nimi: ")
sanat = {"Everybody": nimi1, "Somebody": nimi2, "Anybody": nimi3, "Nobody": nimi4}
with open('data_7a.txt', encoding='utf-8') as f:
    data = f.read()
for vanha, uusi in sanat.items():
    data = data.replace(vanha, uusi)
print(data)