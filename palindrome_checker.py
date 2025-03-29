import re

def is_palindrome(s):
    """Check if the given string is a palindrome (ignores case & special characters)."""
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Remove non-alphanumeric characters & convert to lowercase
    return cleaned_s == cleaned_s[::-1]  # Compare with its reverse

def main():
    print("\n🔄 Welcome to the Palindrome Checker 🔄")

    while True:
        text = input("\nEnter a word or phrase: ").strip()
        
        if is_palindrome(text):
            print(f"✅ '{text}' is a palindrome!")
        else:
            print(f"❌ '{text}' is NOT a palindrome.")

        choice = input("\nDo you want to check another? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("👋 Exiting... Thank you for using the Palindrome Checker!")
            break

if __name__ == "__main__":
    main()
