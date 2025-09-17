import random

def choose_word():
    word_list = ["python", "code", "hangman", "random", "game"]
    return random.choice(word_list)

def display_intro():
    print("=" * 40)
    print("        Welcome to Hangman Game")
    print("=" * 40)
    print("Rules:")
    print("1. You need to guess the hidden word.")
    print("2. You can guess one letter at a time.")
    print("3. You only get 6 wrong attempts.")
    print("4. If you guess all letters, you win!")
    print("=" * 40)

def display_progress(word, guessed_letters):
    progress = ""
    for letter in word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    return progress.strip()

def get_guess(already_guessed):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        if guess in already_guessed:
            print("You already guessed that letter. Try again.")
            continue
        return guess

def play_game():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6

    print("\nLet's start the game!")
    print("The word has", len(word), "letters.")
    print("Word:", "_ " * len(word))

    while wrong_attempts < max_attempts and word_letters:
        print("\nYou have", max_attempts - wrong_attempts, "attempts left.")
        print("Guessed so far:", " ".join(guessed_letters))
        print("Word:", display_progress(word, guessed_letters))
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)
        if guess in word_letters:
            print("Good job! Letter", guess, "is in the word.")
            word_letters.remove(guess)
        else:
            wrong_attempts += 1
            print("Oops! Letter", guess, "is not in the word.")

    if not word_letters:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! You ran out of attempts.")
        print("The word was:", word)

def main():
    display_intro()
    while True:
        play_game()
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != "y":
            print("Thanks for playing! Goodbye.")
            break
        print("\nStarting a new game...\n")

if __name__ == "__main__":
    main()
