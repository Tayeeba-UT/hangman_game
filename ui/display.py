# display.py

def show_welcome():
    print("Welcome to Hangman!")

def choose_category():
    categories = ["Animals", "Countries", "Programming", "Science"]

    print("\nChoose a category:")
    for i, c in enumerate(categories, start=1):
        print(f"  {i}. {c}")

    while True:
        choice = input("\nEnter the number of your choice (1-4): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("Invalid selection. Please choose a number between 1 and 4.")


def show_new_word(category, word_length):
    print(f"New word selected from '{category}' (length {word_length})")
    print("_ " * word_length)

def show_progress(word, guessed_letters, wrong_guesses, max_wrong):
    # Build progress string
    progress = " ".join([ch if ch in guessed_letters else "_" for ch in word])
    print("\nProgress:", progress)
    print("Guessed letters:", ", ".join(guessed_letters) or "None")
    print(f"Remaining attempts: {max_wrong - wrong_guesses}")

def show_result(word, won):
    if won:
        print(f"\nYou win! Word was '{word}'.")
    else:
        print(f"\nYou lost! Word was '{word}'.")
