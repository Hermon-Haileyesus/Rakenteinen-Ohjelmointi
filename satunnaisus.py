import random
print(random.randint(1, 10))  # Outputs a random integer between 1 and 10

print(random.random())  # Outputs a random float between 0.0 and 1.0
print(random.uniform(1.5, 10.5))  # Outputs a random float between 1.5 and 10.5
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))  # Outputs a random fruit from the list
fruits = ["apple", "banana", "cherry", "date"]
print(random.choices(fruits, k=3))  # Outputs a list of 3 random fruits from the list with
deck = ["Ace", "2", "3", "4", "5"]
random.shuffle(deck)
print(deck)  # Outputs the shuffled deck
fruits = ["apple", "banana", "cherry", "date"]
print(random.sample(fruits, k=2))  # Outputs a list of 2 unique random fruits from the list without replacing