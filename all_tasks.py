import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def factorial(n):
    """Find the factorial of a number."""
    if n < 0:
        return "Factorial not defined for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    if n <= 0:
        return "Invalid input! Enter a positive integer."
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def count_vowels_consonants(s):
    """Count vowels and consonants in a string."""
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

def sort_numbers(numbers):
    """Sort a list of numbers."""
    return sorted(numbers)

def find_min_max(numbers):
    """Find the smallest and largest number in a list."""
    return min(numbers), max(numbers)

def main():
    while True:
        print("\n--- Python Task Menu ---")
        print("1. Check if a Number is Prime")
        print("2. Reverse a String")
        print("3. Find Factorial of a Number")
        print("4. Generate Fibonacci Series")
        print("5. Check if a String is a Palindrome")
        print("6. Count Vowels and Consonants in a String")
        print("7. Sort a List of Numbers")
        print("8. Find Smallest and Largest Number in a List")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print(f"Result: {'Prime' if is_prime(num) else 'Not Prime'}")

        elif choice == "2":
            user_str = input("Enter a string: ")
            print(f"Reversed String: {reverse_string(user_str)}")

        elif choice == "3":
            num = int(input("Enter a number: "))
            print(f"Factorial: {factorial(num)}")

        elif choice == "4":
            num = int(input("Enter the number of terms: "))
            print(f"Fibonacci Series: {fibonacci(num)}")

        elif choice == "5":
            user_str = input("Enter a string: ")
            print(f"Palindrome: {'Yes' if is_palindrome(user_str) else 'No'}")

        elif choice == "6":
            user_str = input("Enter a string: ")
            vowels, consonants = count_vowels_consonants(user_str)
            print(f"Vowels: {vowels}, Consonants: {consonants}")

        elif choice == "7":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            print(f"Sorted List: {sort_numbers(numbers)}")

        elif choice == "8":
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            smallest, largest = find_min_max(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif choice == "9":
            print("Exiting... Goodbye! 👋")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
