from pathlib import Path
from datetime import datetime
from game.wordlist import get_random_word
from ui.display import show_welcome, choose_category, show_new_word, show_progress, show_result
from game.logger import log_game
from game.ascii_art import HANGMAN_STAGES


def start_game():
    """Play one round of Hangman (with categories and scoring)."""
    show_welcome()
    category = choose_category() or "General"
    word = get_random_word(category)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    show_new_word(category, len(word))

    while wrong_guesses < max_wrong:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a–z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1

        show_progress(word, guessed_letters, wrong_guesses, max_wrong)
        print(HANGMAN_STAGES[wrong_guesses])

        if all(ch in guessed_letters for ch in word):
            won = True
            break
    else:
        won = False

     # --- Scoring and stats ---
    score = calculate_score(word, wrong_guesses) if won else 0
    show_result(word, won)
    print(f"Points earned this round: {score}")

    update_stats(won, score)

    # --- Logging (after updating stats) ---
    total_score = get_total_score()
    log_game(category, word, guessed_letters, wrong_guesses, won, score, total_score)


def calculate_score(word, wrong_guesses):
    """Length × 10 − wrong_guesses × 5"""
    return len(word) * 10 - wrong_guesses * 5


def update_stats(won, score):
    """Read, update, and write stats to stats.txt"""
    stats_path = Path(__file__).parent.parent / "stats.txt"

    # Read existing stats
    if stats_path.exists():
        with open(stats_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = []

    # Convert existing stats to a dictionary
    stats = {"games": 0, "wins": 0, "losses": 0, "total_score": 0}
    for line in lines:
        key, val = line.split(":")
        stats[key.strip()] = float(val.strip())

    # Update
    stats["games"] += 1
    if won:
        stats["wins"] += 1
        stats["total_score"] += score
    else:
        stats["losses"] += 1

    # Derived metrics
    win_rate = (stats["wins"] / stats["games"]) * 100 if stats["games"] else 0
    avg_score = stats["total_score"] / stats["games"] if stats["games"] else 0

    # Save back
    with open(stats_path, "w") as f:
        f.write(f"games: {stats['games']}\n")
        f.write(f"wins: {stats['wins']}\n")
        f.write(f"losses: {stats['losses']}\n")
        f.write(f"total_score: {stats['total_score']}\n")
        f.write(f"win_rate(%): {win_rate:.2f}\n")
        f.write(f"average_score_per_game: {avg_score:.2f}\n")

    # Show summary
    print(f"\nGames played: {int(stats['games'])}")
    print(f"Wins: {int(stats['wins'])} | Losses: {int(stats['losses'])}")
    print(f"Total score: {int(stats['total_score'])}")
    print(f"Win rate: {win_rate:.2f}% | Average score per game: {avg_score:.2f}")


def get_total_score():
    """Reads total_score from stats.txt for logging."""
    stats_path = Path(__file__).parent.parent / "stats.txt"
    if not stats_path.exists():
        return 0
    with open(stats_path, "r") as f:
        for line in f:
            if line.startswith("total_score"):
                return int(float(line.split(":")[1].strip()))
    return 0
