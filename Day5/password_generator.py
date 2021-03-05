# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
# Find letters
for index in range(0, nr_letters):
    character = random.choice(letters)
    password += character

# Find symbols
for index in range(0, nr_symbols):
    character = random.choice(symbols)
    password += character

# Find numbers
for index in range(0, nr_numbers):
    character = random.choice(numbers)
    password += character
print(f"Your easy password would be: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list_password_character = []
for index in range(0, nr_letters):
    character = random.choice(letters)
    list_password_character.append(character)

# Find symbols
for index in range(0, nr_symbols):
    character = random.choice(symbols)
    list_password_character.append(character)

# Find numbers
for index in range(0, nr_numbers):
    character = random.choice(numbers)
    list_password_character.append(character)
# Re-order list character with random order
random.shuffle(list_password_character)

password = ""
for character in list_password_character:
    password += character
print(f"Your hard password version would be: {password}")