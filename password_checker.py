import re
import math
import random
import string

def calculate_entropy(password):
    """Calculate the entropy of a password (higher is better)."""
    character_set_size = 0

    if any(c.islower() for c in password):
        character_set_size += 26  # a-z
    if any(c.isupper() for c in password):
        character_set_size += 26  # A-Z
    if any(c.isdigit() for c in password):
        character_set_size += 10  # 0-9
    if any(c in string.punctuation for c in password):
        character_set_size += len(string.punctuation)  # Special characters

    entropy = len(password) * math.log2(character_set_size) if character_set_size > 0 else 0
    return entropy

def check_password_strength(password):
    """Evaluates the strength of a password based on various factors."""
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Password Strength Scoring
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if length >= 16:
        score += 1  # Bonus for extra-long passwords

    # Password Strength Categories
    entropy = calculate_entropy(password)
    
    if score <= 2:
        strength = "❌ Weak"
    elif score == 3:
        strength = "⚠️ Moderate"
    elif score == 4:
        strength = "✅ Strong"
    else:
        strength = "💪 Very Strong"

    return strength, entropy

def suggest_improvements(password):
    """Provides suggestions to make a password stronger."""
    suggestions = []
    if len(password) < 8:
        suggestions.append("Increase length to at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Include at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include at least one special character (e.g., @, #, $).")

    return suggestions if suggestions else ["Your password is strong!"]

def generate_strong_password(length=16):
    """Generates a strong password of the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def main():
    """Main function to check password strength."""
    while True:
        print("\n🔐 Password Strength Checker")
        print("1️⃣ Check Password Strength")
        print("2️⃣ Generate Strong Password")
        print("3️⃣ Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            password = input("\nEnter your password: ").strip()
            strength, entropy = check_password_strength(password)
            print(f"\n🔎 Password Strength: {strength}")
            print(f"📊 Entropy Score: {entropy:.2f} bits (Higher is better)")
            
            suggestions = suggest_improvements(password)
            print("\n💡 Suggestions for Improvement:")
            for suggestion in suggestions:
                print(f"  - {suggestion}")

        elif choice == "2":
            new_password = generate_strong_password()
            print(f"\n🛠️ Generated Strong Password: {new_password}")

        elif choice == "3":
            print("👋 Exiting... Stay secure!")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
