"""A small, text-based Hangman game for beginner Python programmers."""

import random


WORDS = ["python", "apple", "planet", "coding", "school"]
MAX_WRONG_GUESSES = 6


def show_word(secret_word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word one letter at a time. You can make {MAX_WRONG_GUESSES} wrong guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES and not all(
        letter in guessed_letters for letter in secret_word
    ):
        print(f"\nWord: {show_word(secret_word, guessed_letters)}")
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (A-Z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("That letter is not in the word.")

    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nYou win! The word was: {secret_word}")
    else:
        print(f"\nYou ran out of guesses. The word was: {secret_word}")


if __name__ == "__main__":
    play_game()
