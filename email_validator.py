import re

# Regex pattern for email validation
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """Check if the given email is valid."""
    return re.match(EMAIL_REGEX, email) is not None

def validate_single_email():
    """Validate a single email input from the user."""
    email = input("Enter an email address to validate: ").strip()
    if is_valid_email(email):
        print(f"✅ '{email}' is a valid email address.")
    else:
        print(f"❌ '{email}' is NOT a valid email address.")

def validate_bulk_emails_from_file(input_file, output_file):
    """Validate multiple emails from a file and save results."""
    try:
        with open(input_file, 'r') as file:
            emails = file.readlines()

        valid_emails = []
        invalid_emails = []

        for email in emails:
            email = email.strip()
            if is_valid_email(email):
                valid_emails.append(email)
            else:
                invalid_emails.append(email)

        # Save results to a file
        with open(output_file, 'w') as file:
            file.write("✅ Valid Emails:\n")
            file.write("\n".join(valid_emails))
            file.write("\n\n❌ Invalid Emails:\n")
            file.write("\n".join(invalid_emails))

        print(f"\nResults saved to '{output_file}'")
        print(f"✅ Valid emails found: {len(valid_emails)}")
        print(f"❌ Invalid emails found: {len(invalid_emails)}")

    except FileNotFoundError:
        print(f"❌ Error: File '{input_file}' not found!")

def main():
    """Main menu for email validation."""
    while True:
        print("\n📧 Email Validation System")
        print("1. Validate a Single Email")
        print("2. Validate Multiple Emails from a File")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            validate_single_email()
        elif choice == "2":
            input_file = input("Enter the file name containing emails: ").strip()
            output_file = "validated_emails.txt"
            validate_bulk_emails_from_file(input_file, output_file)
        elif choice == "3":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
