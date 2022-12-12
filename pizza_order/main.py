# Prompt
print("Welcome to the OYALO pizza!.. ")

price_amount: int = 25

size = input("What size of pizza do you want s, m, l?. ")
add_pepporoni = input("Do you want pepporoni? ")
extra_cheese = input("Do you want Extra cheese ")

 # If-Else Statement
if size == "s":
  price_amount = 15
  print("The price of the Small pizza is $15. ")
elif size == "m":
  price_amount = 20
  print("The price of the Medium pizza is $20. ")
else:
  print("The price of the Large pizzza is $25.  ")

# Add pepporoni
if add_pepporoni == "y":
  print("size: ", size)
  if size == "s":
    price_amount += 2
  else:
    price_amount += 3

# Add extra cheese
if extra_cheese == "y":
  price_amount += 1
  print(f"The Final bill is ${price_amount}. ")
else:
  print(f"The Final bill is ${price_amount}. ")
