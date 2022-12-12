# Treasure Game 

picture = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

# Prompt function
print(picture)
print("Welcome to the Treasure Island.. ")
print("Your mission is to find the treasure. ")

# Give the question to user
way = input('You are at a cross road.Where do you want to go? Type "left" or "right" ')

if (way == "left"):
    lake_selection = input('You come to a lake.There is an island in the middle of the lake.Type "wait" wait for a boat.Type "swim" to swim across')
    if (lake_selection == "wait"):
        door_selection = input("You arrive at the island unharmed.There is a house with 3 doors. One red, one yellow and one blue.Which colour do you choose? ")
        if (door_selection == "red"):
            print("You enter a room of Fire!..\n Game Over.... ")
        elif (door_selection == "yellow"):
            print("Congratulations..\n You won the Treasure... ")
        elif (door_selection == "blue"):
            print("You enter a room of Beast!..\n Game Over.... ")
        else :
            print("Enter valid input.. ")
    elif (lake_selection == "swim"):
        print("You may wait for a boat.\n Game Over.. ")        
    else:
        print("Enter valid input.. ")
elif (way == "right"):
    print("Game Over.. ")
else:
    print("Enter valid input.. ")