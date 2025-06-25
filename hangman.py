#hangman game
import random
def get_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words) 
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           
           
           
           
           
        -"""
    ]
    return stages[tries]
def play_hangman():     
    word = get_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! That letter is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print("Sorry, that word is not correct.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please try again.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations! You guessed the word: " + word)
    else:
        print("Sorry, you ran out of tries. The word was: " + word)
if __name__ == "__main__":
    play_hangman()
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            play_hangman()
        elif play_again == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    print("Exiting the game.")
    exit(0) 

    