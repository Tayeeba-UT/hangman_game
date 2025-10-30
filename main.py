# main.py
from game.engine import start_game
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        start_game()
        again = input("\nDo you want to play another round? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing Hangman! Goodbye.")
            break

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
