# Python Password Generator

# import function 
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
           "r", "s", "t","u", "v","w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V","W", "X", "Y", "Z"]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']



# Prompt function
print("Welcome to the PyPassword Generator! ")


# input
user_letters = int(input("How many letters would you like in your password?\n "))

user_symbols = int(input("How many symbols would you like?\n "))

user_numbers = int(input("How many numbers would you like?\n "))

password = ""

for char in range(1, user_letters +1):
    random_char = random.choice(letters)
    password += random_char

for char in range(1, user_symbols +1):
    random_symbols = random.choice(symbols)
    password +=random_symbols

for char in range(1, user_symbols +1):
    random_numbers = random.choice(numbers)
    password += random_numbers

print(f"Here is your password: {password} ")
