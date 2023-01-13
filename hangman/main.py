


import random


stages = [
"""      
        
    +----+
    |    |
    O    |
   /|\   |
   / \   |
         |
==========
""",

"""
    +----+
    |    |
    O    |
   /|\   |
   /    |
         |
==========""",
""" 
    +----+
    |    |
    O    |
   /|\   |
         |
         |
=========="""

"""
    +----+
    |    |
    O    |
   /|    |
         |
         |
==========""",

"""
    +----+
    |    |
    O    |
    |    |
         |
         |
==========""",

"""
    +----+
    |    |
    O    |
         |
         |
         |
==========""",
"""
    +----+
    |    |
         |
         |
         |
         |
==========""",
]
logo =["""
     _
    | |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
    | '_ \ / _' | '_ \ / _' | '_ '   \ / _' | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       ___/ |
                      |_____/
"""]

lives = 6

display = []

word_list = ['apple', 'orange', 'jackfruit','pinapple','custardapple','greenapple']

# Choose a random word in a word_list
chosen_word = random.choice(word_list)

word_length = len(chosen_word)


for  i in range(word_length):
    display += "-"

print(display)

end_of_game = False


while not end_of_game:
    
    # Get the user guess character
    guess = input("Guess a letter of the fruit: ").lower() 
 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose....")
    
    print(display)

    if "-" not in display:
        end_of_game = True
        print("You win....") 
    print(stages[lives])