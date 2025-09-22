# Guess the Number — Fun CLI Game
import random

def choose_range(level):
    """Return range and attempts based on level"""
    if level == "1":   # Easy
        return 1, 30, 10
    elif level == "2": # Medium
        return 1, 100, 7
    else:              # Hard
        return 1, 500, 10

def play_round():
    print("Choose a level — 1) Easy  2) Medium  3) Hard")
    level = input("Enter level number (1/2/3): ").strip()
    if level not in {"1","2","3"}:
        print("Invalid choice — defaulting to Medium.")
        level = "2"

    low, high, max_attempts = choose_range(level)
    target = random.randint(low, high)

    print(f"\nI have a number in mind between {low} and {high}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts} — Your guess: ").strip())
        except ValueError:
            print("Please enter a valid integer. This counts as an attempt.")
            continue

        if guess == target:
            print("\n🎉 Congratulations! You guessed it right!")
            score = max(0, (max_attempts - attempts + 1) * 10)
            print(f"Attempts taken: {attempts}, Your score: {score}")
            break
        elif guess <= target:
            print("The number is higher. Try again.")
        else:
            print("The number is lower. Try again.")

        # Hint
        if attempts == max_attempts // 2:
            dist = abs(guess - target)
            if dist <= (high - low) * 0.05:
                print("Hint: Very close!")
            elif dist <= (high - low) * 0.15:
                print("Hint: Moderately close.")
            else:
                print("Hint: Still far away.")

    else:
        # If loop finishes without break
        print("\n 😥Sorry, you're out of attempts.")
        print(f"The number I had in mind was: {target}")

def main():
    print("=== Guess the Number — Fun Game ===")
    while True:
        play_round()
        again = input("\n Do you want to play again?😊 (y/n): ").strip().lower()
        if again not in {"y","yes"}:
            print("Thanks for playing! See you next time 🚀")
            break

if __name__ == "__main__":
    main()
