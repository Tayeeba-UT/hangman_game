# wordlist.py
import random
from pathlib import Path

def get_random_word(category=None):
    """Reads words from category file if available, otherwise from words.txt."""
    base_path = Path(__file__).parent.parent / "words"
    categories_folder = base_path / "categories"

    # Normalize input (lowercase, strip spaces)
    if category:
        category = category.strip().lower()
    else:
        category = ""

    # Build possible file names
    category_file = categories_folder / f"{category}.txt"
    alt_category_file = categories_folder / f"{category}s.txt"  # plural fallback

    # Decide which file to read
    if category and category_file.exists():
        path = category_file
    elif category and alt_category_file.exists():
        path = alt_category_file
    else:
        print(f"(No category file found for '{category}', using default list.)")
        path = default_file

    # Load words
    try:
        with open(path, "r") as f:
            words = [w.strip() for w in f if w.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find {path}")
        return "python"  # fallback default

    # Choose one random word
    return random.choice(words)
