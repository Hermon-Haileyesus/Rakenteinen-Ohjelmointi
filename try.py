txt = "welcome to the jungle"

x = txt.split()

print(x)
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

text = """This is the first line.
This is the second line.
This is the third line."""

lines = text.split('\n') #The '\n' character represents a newline, so this method will break the string at each newline and create a list of lines.
print(lines) 
newlines_count = text.count('\n')
print(newlines_count)
txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)
text = """This is the first line.
This is the second line.
This is the third line."""

search_word = "second"
position = text.find(search_word)

# Calculate the line position
line_position = position - text.rfind('\n', 0, position) - 1

print(f"The word '{search_word}' appears at character position {line_position} within its line.")
text = """This is the first line.
This is the second line.
This is the third line love."""

search_word = "love"
position = text.find(search_word)
lin = text.rfind('\n', 0, position)
line_position = position - text.rfind('\n', 0, position) - 1
print(lin)
print(position)
print(f"The word '{search_word}' appears at character position {line_position} within its line.")

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
