def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("\n🌡️ Temperature Conversion Program 🌡️")
    
    while True:
        print("\nChoose an option:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        elif choice == "3":
            print("Exiting... Stay cool! ❄️🔥")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
