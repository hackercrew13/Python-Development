import random
import time
import json

LEADERBOARD_FILE = "number_guess_leaderboard.json"

def load_leaderboard():
    """Load leaderboard from file or create a new one."""
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_leaderboard(leaderboard):
    """Save the leaderboard to a file."""
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

def get_difficulty():
    """Let the user select a difficulty level."""
    while True:
        print("\n🎯 Select Difficulty Level:")
        print("1️⃣ Easy (1-50) 🔹")
        print("2️⃣ Medium (1-100) 🔹🔹")
        print("3️⃣ Hard (1-200) 🔹🔹🔹")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            return (1, 50, "Easy")
        elif choice == "2":
            return (1, 100, "Medium")
        elif choice == "3":
            return (1, 200, "Hard")
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

def ai_hint(secret, guess, min_num, max_num):
    """Generate smart AI hints based on guess proximity."""
    diff = abs(secret - guess)

    if diff == 0:
        return "🎯 Correct!"
    elif diff <= 3:
        return "🔥 Super close!"
    elif diff <= 10:
        return "🔍 Very close!"
    elif diff <= 20:
        return "👀 Getting warmer..."
    elif guess < secret:
        return f"📉 Too low! Try between {guess + 1} and {max_num}."
    else:
        return f"📈 Too high! Try between {min_num} and {guess - 1}."

def play_game():
    """Main function to play the number guessing game."""
    min_num, max_num, level = get_difficulty()
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    start_time = time.time()

    print(f"\n🎮 You have chosen {level} mode!")
    print(f"🔢 I have selected a number between {min_num} and {max_num}. Try to guess it!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < min_num or guess > max_num:
                print(f"❌ Out of range! Enter a number between {min_num} and {max_num}.")
                continue

            hint = ai_hint(secret_number, guess, min_num, max_num)
            print(hint)

            if guess == secret_number:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                score = max(1000 - (attempts * 10) - int(total_time * 2), 0)

                print(f"\n🎉 You guessed the number {secret_number} in {attempts} attempts!")
                print(f"⏱️ Time taken: {total_time} seconds")
                print(f"🏆 Your score: {score} points")

                update_leaderboard(level, attempts, total_time, score)
                break

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def update_leaderboard(level, attempts, time_taken, score):
    """Update and display the leaderboard."""
    leaderboard = load_leaderboard()

    if level not in leaderboard or leaderboard[level]['score'] < score:
        leaderboard[level] = {"attempts": attempts, "time": time_taken, "score": score}
        print(f"\n🎖️ New High Score in {level} Mode! 🏆")
    else:
        print(f"\n🥈 Your score: {score}, Best score in {level}: {leaderboard[level]['score']}")

    save_leaderboard(leaderboard)

def show_leaderboard():
    """Display the leaderboard."""
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("\n📜 No high scores recorded yet.")
        return

    print("\n🏆 Leaderboard 🏆")
    for level, stats in leaderboard.items():
        print(f"🔹 {level} Mode: {stats['score']} points (⏱️ {stats['time']} sec, {stats['attempts']} attempts)")

def main():
    """Main menu for the game."""
    while True:
        print("\n🎮 Number Guesser Game 🎯")
        print("1️⃣ Play Game")
        print("2️⃣ View Leaderboard 🏆")
        print("3️⃣ Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("👋 Exiting... Thanks for playing!")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
