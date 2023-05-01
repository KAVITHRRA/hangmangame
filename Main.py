import random

word_list = ["priest", "hauntingadeline", "doesithurt", "stillbeating", "silluv", "flock", "therearenosaints"]
hangman_pics = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]



def get_word():
    return random.choice(word_list)



def display_game(word, guesses, incorrect_guesses):
    
    print(hangman_pics[len(incorrect_guesses)])

    
    displayed_word = "".join([letter if letter in guesses else "_" for letter in word])
    print(displayed_word)

    
    remaining_guesses = max_guesses - len(incorrect_guesses)
    print("Remaining guesses:", remaining_guesses)



word = get_word()
max_guesses = 10
guesses = set()
incorrect_guesses = set()


while True:
    display_game(word, guesses, incorrect_guesses)

    
    if all(letter in guesses for letter in word):
        print("You win!")
        break

    
    if len(incorrect_guesses) == max_guesses:
        print("You lose! The word was", word)
        break

    
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha() or guess in guesses.union(incorrect_guesses):
        print("Invalid guess. Please guess a single letter that you haven't guessed before.")
        continue

    
    if guess in word:
        guesses.add(guess)
        print("Correct!")
    else:
        incorrect_guesses.add(guess)
        print("Incorrect!")
        
