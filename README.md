# Hangman Game

A simple, terminal-based version of the classic Hangman puzzle — built completely in Python with no external libraries.  
The project was developed to practice modular programming, file handling, and clean code structure, but it’s also just fun to play.

---

## What It Does

When you run the game, you’ll be asked to choose a category — **Animals**, **Countries**, **Programming**, or **Science**.  
A random word from that category is selected, and you guess one letter at a time.  
Each wrong guess adds a piece to the hangman drawing. Six wrong guesses, and you’re out.

The game keeps track of your total score and win rate, creates a log for every round, and saves all your progress between runs.

---

## How to Run

1. Make sure you have **Python 3.9** or later installed.  
2. Download or clone this repository:
   ```bash
   git clone https://github.com/yourusername/hangman_game.git
   cd hangman_game
Start the game from the terminal:

bash
Copy code
python main.py
Follow the on-screen instructions to pick a category and start guessing.

You can play as many rounds as you like — your statistics will update automatically after each one.

Scoring Rules
Each correct word earns points based on its length and how many mistakes you made:

ini
Copy code
Score = (word_length × 10) − (wrong_guesses × 5)
A loss gives 0 points for that round.
Your cumulative stats (games played, wins, losses, total score, win rate, and average score per game) are stored in stats.txt.

Word Lists
All words are stored as plain text — one per line.

bash
Copy code
words/
├── words.txt             # General list (fallback)
└── categories/
    ├── animals.txt
    ├── countries.txt
    ├── programming.txt
    └── science.txt
You can easily expand these files or add your own categories.
For example, create movies.txt inside words/categories/ and the game will pick it up automatically.

Game Logs
Every round is recorded inside the game_log folder.
Each game gets its own sub-folder:

bash
Copy code
game_log/
├── game1/log.txt
├── game2/log.txt
└── ...
Each log.txt file includes:

Category and word used

All guesses (correct and incorrect)

Number of wrong guesses

Result (Win or Loss)

Points for the round

Date and time

A small readme.txt in that folder explains its purpose if it’s empty.

Folder Overview
bash
Copy code
hangman_game/
├── main.py                   # Entry point
├── stats.txt                 # Persistent stats
├── README.md                 # This file
├── words/                    # Wordlists and categories
├── game/                     # Core logic
│   ├── engine.py
│   ├── wordlist.py
│   ├── ascii_art.py
│   └── logger.py
├── ui/                       # Terminal display functions
│   └── display.py
└── game_log/                 # Auto-generated logs
Customizing the Game
Add new categories:
Create a .txt file inside words/categories/ and fill it with one word per line.

Change the scoring formula:
Edit calculate_score() in engine.py.

Update ASCII art:
Modify the drawings in ascii_art.py.

Reset your progress:
Delete or clear stats.txt.

Everything runs with basic Python functions — no packages or frameworks required.

Requirements
Python 3.9 +

Works entirely in the terminal

Uses only standard library modules (pathlib, random, datetime, os)

Example Gameplay
markdown
Copy code
=============================================
           WELCOME TO HANGMAN
=============================================
Choose a category:
  1. Animals
  2. Countries
  3. Programming
  4. Science

Enter the number of your choice (1-4): 3

New word selected from 'Programming' (length 6)
_ _ _ _ _ _
Guessed letters: None
Remaining attempts: 6

Enter a letter: p
Correct!
---------------------------------------------
Word: p _ _ _ _ _
Guessed letters: p
Remaining attempts: 6
---------------------------------------------
Author
Umbreen Tariq
Advanced Python Programming Course
