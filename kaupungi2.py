import random

# kaupungit.py
oikeinlkm = 0  # Initialize the correct answers count
total_questions = 0  # Initialize the total questions count

with open('pkaupungit.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

random.shuffle(lines)  # Shuffle the list of lines

for line in lines:
    line = line.strip()
    parts = line.split('?')
    country = parts[0]
    correct_capital = parts[1]
    
    response = input(f'Maan nimi on {country}. Anna pääkaupunki (quit = lopetus): ')
    
    if response.lower() == 'quit':
        break
    
    total_questions += 1
    
    if response == correct_capital:
        print('Oikein!')
        oikeinlkm += 1
    else:
        print(f'Väärin! oikea vastaus olisi ollut {correct_capital}')

if total_questions > 0:
    success_rate = (oikeinlkm / total_questions) * 100
    print(f'Oikein vastattuja kysymyksiä: {oikeinlkm}')
    print(f'Onnistumisprosentti: {success_rate:.2f}%')
else:
    print('Ei yhtään kysymystä vastattu.')