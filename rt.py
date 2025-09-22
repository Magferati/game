# Guess the Number — মজার CLI গেম
# চালাতে: python guess_game.py

import random

def choose_range(level):
    """লেভেল অনুযায়ী রেঞ্জ এবং অনুমোদিত চেষ্টা ফেরত দেয়"""
    if level == "1":   #easy
        return 1, 30, 10
    elif level == "2": # mediam
        return 1, 100, 7
    else:              # heard
        return 1, 500, 10

def play_round():
    print("chose your level — 1) easy  2) mediem 3) heard")
    level = input("level number (1/2/3) input: ").strip()
    if level not in {"1","2","3"}:
        print("Didn't like it — defaulting to Medium." )
        level = "2"
    low, high, max_attempts = choose_range(level)
    target = random.randint(low, high)

    print(f"\n You have a number in my mind {low} to {high} guess the number")
    print(f"you have totel {max_attempts}live . all the best\n")

    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"try {attempts}/{max_attempts} — your guess: ").strip())
        except ValueError:
            print("kindly enter a valid number")
            continue

        if guess == target:
            print("\n🎉 wow! all right — you win!")
            score = max(0, (max_attempts - attempts + 1) * 10)
            print(f"Attempts taken: {attempts}, your score: {score}")
            break
        elif guess < target:
            print("answer is big. Try again.")
        else:
            print("answer is small. Try again.")

        # ছোট হালকা হিন্ট (সতর্কভাবে)
        if attempts == max_attempts // 2:
            dist = abs(guess - target)
            if dist <= (high - low) * 0.05:
                print("hint: your guess is very close")
            elif dist <= (high - low) * 0.15:
                print("hint: somewhat close")
            else:
                print("hint: you are so far")

    else:
        # লুপ পুরো শেষ হলে (জেতার আগেই চেষ্টা শেষ)
        print("\n 😥sorry  — you're out of attempts.")
        print(f"The number I had in mind was: {target}")

def main():
    print("=== Guess the Number — funny game ===")
    while True:
        play_round()
        again = input("\n play it again? (y/n): ").strip().lower()
        if again not in {"y","yes"}:  # 'আঁ' বাংলা ছোট 'হ্যাঁ' নয়; শুধু উদাহরণ
            print("Thanks for play! see you again 🚀")
            break

if __name__ == "__main__":
    main()
