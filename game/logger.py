# logger.py
from pathlib import Path
from datetime import datetime

def log_game(category, word, guessed_letters, wrong_guesses, won, score, total_score):
    """Creates a new log folder and saves details of this game."""
    base_log = Path(__file__).parent.parent / "game_log"

    # Count existing game folders to name the next one
    existing = [f for f in base_log.iterdir() if f.is_dir()]
    game_num = len(existing) + 1
    game_folder = base_log / f"game{game_num}"
    game_folder.mkdir(parents=True, exist_ok=True)

    log_file = game_folder / "log.txt"

    correct = [g for g in guessed_letters if g in word]
    wrong = [g for g in guessed_letters if g not in word]

    with open(log_file, "w", encoding="utf-8") as f:

        f.write(f"Game {game_num} Log\n")
        f.write(f"Category: {category}\n")
        f.write(f"Word: {word}\n")
        f.write(f"Word Length: {len(word)}\n\n")

        f.write("Guesses (in order):\n")
        for i, g in enumerate(guessed_letters, 1):
            result = "Correct" if g in word else "Wrong"
            f.write(f"{i}. {g} -> {result}\n")


        f.write("\nWrong Guesses List: " + ", ".join(wrong) + "\n")
        f.write(f"Wrong Guesses Count: {wrong_guesses}\n")
        f.write(f"Result: {'Win' if won else 'Loss'}\n")
        f.write(f"Points Earned: {score}\n")
        f.write(f"Total Score (after this round): {total_score}\n")
        f.write(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"\nGame log saved: {log_file}")
