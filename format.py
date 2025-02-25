name = "Alice"
age = 30
text = "My name is {} and I am {} years old.".format(name, age)
print(text)
text = "The {0} is {1} and {2} is {1}".format("sky", "blue", "ocean")
print(text)
text = "My favorite fruit is {fruit} and my favorite color is {color}".format(fruit="apple", color="red")
print(text)
pi = 3.141592653589793
text = "Pi to three decimal places is {:.3f}".format(pi)
print(text)
text = "{:<10} | {:^10} | {:>10}".format("left", "center", "right")
print(text)
data = {"name": "Alice", "age": 30}
text = "My name is {name} and I am {age} years old.".format(**data) #format(name=data["name"], age=data["age"]) same as **data
print(text)

