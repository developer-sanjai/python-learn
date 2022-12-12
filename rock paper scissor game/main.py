# Rock Paper Scissor game

# import random
import random

# prompt 
print("Hi...Welcome to Game! ")
rock = '''  
     _______
---'   ___ _)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper =  ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissor]

# input
user_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper,2 for Scissors. \n"))
print(game_images[user_choice])

# Computer choice
computer_choice = random.randint(0, 2)
print(f"Computer choose:{game_images[computer_choice]}")


if (user_choice >= 3 or user_choice < 0):
    print("You typed an invalid number,you lose! ")
elif(user_choice == 0 and computer_choice == 2):
    print("You win.. ")
elif(user_choice == 2 and computer_choice == 0):
    print("You lose!.. ")
elif (computer_choice > user_choice):
    print("You lose!.. ")
elif (user_choice > computer_choice):
    print("You win.. ")
elif (user_choice == computer_choice):
    print("It's a draw ")



