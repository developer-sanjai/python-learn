import hangman_arts
import hangman_words
import random


# Prompt 
print(hangman_arts.logo)

lives = 6

display = []


# Choose a random word in a word_list
chosen_word = random.choice(hangman_words.word_list)

# Assign a length of a choosen word in a word_length
word_length = len(chosen_word)

# Creating a loop 
for  i in range(word_length):
    display += "-"

print(display)

# Identify the game status
end_of_game = False


while not end_of_game:
    
    # Get the user guess character
    guess = input("Guess a letter: ").lower() 

    if guess in display:
        print(f"You've already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose a life. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose...")
            
    
    print(display)

    if "-" not in display:
        end_of_game = True
        print("You win....") 
    
    print(hangman_arts.stages[lives])