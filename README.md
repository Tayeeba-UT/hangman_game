# Hangman Game

A modular, terminal-based Hangman game written in pure Python.  
This project was developed for an academic assignment focused on file handling, modular programming, and clean code organization.  
It can be easily reused or extended by anyone learning Python fundamentals.

---

## Features

- Fully terminal-based word guessing game  
- Category selection (Animals, Countries, Programming, Science)  
- Scoring system with persistent statistics  
- Automatic logging of every game  
- Seven-stage ASCII-art hangman display  
- Built using only basic Python concepts — no external libraries, no classes

---

## Getting Started

### 1. Clone or Download

Clone this repository or download it as a ZIP file.

```bash
git clone https://github.com/yourusername/hangman_game.git
cd hangman_game
2. Run the Game
Make sure Python 3.9 or newer is installed, then run:

bash
Copy code
python main.py
The game will launch in your terminal.

Folder Structure
bash
Copy code
hangman_game/
├── main.py                   # Entry point
├── stats.txt                 # Persistent statistics
├── words/
│   ├── words.txt             # Default wordlist (one word per line)
│   └── categories/
│       ├── animals.txt
│       ├── countries.txt
│       ├── programming.txt
│       └── science.txt
├── game/
│   ├── engine.py             # Main game loop and logic
│   ├── wordlist.py           # Word loading and random selection
│   ├── ascii_art.py          # Hangman ASCII drawings
│   └── logger.py             # Handles per-game logging
├── ui/
│   └── display.py            # UI and terminal output functions
└── game_log/
    └── game1/log.txt         # Example of a generated game log
How It Works
Category Selection
The player chooses a category at startup.
Words are loaded from words/categories/<category>.txt, or from words.txt if the category file is missing.

Gameplay Loop
The player has six wrong attempts to guess the word, one letter at a time.
Each incorrect guess progresses the ASCII-art hangman.

Scoring System
ini
Copy code
Score = (word_length × 10) − (wrong_guesses × 5)
Losing a round gives 0 points.

Persistent Statistics
Overall statistics are saved in stats.txt and updated automatically:

Games played

Wins and losses

Total score

Win rate (%)

Average score per game

Game Logging
Each new round creates a folder inside game_log/:

bash
Copy code
game_log/game1/log.txt
game_log/game2/log.txt
Each log file records category, word, guesses, result, score, and timestamp.

Customization
Add More Categories
Create new text files inside words/categories/ (for example, movies.txt, sports.txt).
Each line should contain one word.

Change ASCII Art
Modify drawings in game/ascii_art.py.

Adjust Scoring Rules
Edit the calculate_score() function inside engine.py.

Requirements
Python 3.9 or later

No external dependencies (uses only the Python standard library)

License
This project is open-source and free for educational or personal use.
You may modify and extend it for learning or demonstrations.

Acknowledgment
Developed as part of the Advanced Python Programming course to demonstrate:

Functions and Type Hinting

File Handling and Path Management

Control Flow and Loops

Lists, Dictionaries, and Sets

Modular Code Organization

Example Gameplay (Terminal Output)
vbnet
Copy code
Welcome to Hangman!
Choose a category (Animals, Countries, Programming, Science):
> Programming
New word selected from 'Programming' (length 6)
_ _ _ _ _ _
Guessed letters: None
Remaining attempts: 6

Enter a letter: p
Correct!
Progress: p _ _ _ _ _
Remaining attempts: 6
Anyone cloning this repository can immediately run python main.py to start playing or extend the logic for their own projects.

Author
Umbreen Tariq