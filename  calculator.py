def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "❌ Error: Modulus by zero!"
    return a % b

def calculator():
    print("\n🔢 Welcome to the Python Calculator 🔢")
    
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            operator = input("Enter an operator (+, -, *, /, %): ").strip()
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '%':
                result = modulus(num1, num2)
            else:
                print("❌ Invalid operator! Please use +, -, *, /, or %.")
                continue

            print(f"✅ Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("❌ Error: Please enter valid numeric values.")

        choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("👋 Exiting... Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()
