import random
import re
from collections import Counter
def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100
    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue
        attempts += 1
        if guess < secret_number:
            score = max(0, score - 10)
            print("Too low! Try again.")
        elif guess > secret_number:
            score = max(0, score - 10)
            print("Too high! Try again.")
        else:
            print("\nCorrect! You guessed the number.")
            print("Attempts:", attempts)
            print("Final score:", score)
            break
def word_frequency():
    print("\n=== WORD FREQUENCY ANALYZER ===")
    filename = input("Enter the text file name: ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
        print("Could not read the file:", error)
        return
    words = re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())
    if not words:
        print("The file is empty or contains no words.")
        return
    word_counts = Counter(words)
    print("\nTotal words:", len(words))
    print("Unique words:", len(word_counts))
    print("\nTop 10 most common words:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")
def main():
    while True:
        print("\n===== MINI PYTHON TOOLS =====")
        print("1. Number Guessing Game")
        print("2. Word Frequency Analyzer")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            guessing_game()
        elif choice == "2":
            word_frequency()
        elif choice == "3":
            print("Thanks for using Mini Python Tools!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()