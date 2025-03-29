def fibonacci_recursive(n):
    """Generate Fibonacci sequence using recursion (not optimized for large n)."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

def fibonacci_iterative(n):
    """Generate Fibonacci sequence using iteration (optimized for large n)."""
    fib_seq = [0, 1]
    for _ in range(n - 2):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def fibonacci_memoization(n, memo={0: 0, 1: 1}):
    """Generate Fibonacci sequence using memoization for efficiency."""
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_generator(n):
    """Generate Fibonacci sequence using a generator (memory efficient)."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def fibonacci_pattern(n):
    """Print Fibonacci numbers in a formatted pyramid pattern."""
    fib_list = fibonacci_iterative(n)
    for i in range(1, n + 1):
        print(" ".join(map(str, fib_list[:i])))

def main():
    """Main function to provide different Fibonacci sequence options."""
    while True:
        print("\n🔢 Fibonacci Sequence Generator")
        print("1️⃣ Recursive Method (Slow for large n)")
        print("2️⃣ Iterative Method (Fast)")
        print("3️⃣ Memoization (Optimized Recursion)")
        print("4️⃣ Generator Method (Memory Efficient)")
        print("5️⃣ Fibonacci Pattern")
        print("6️⃣ Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                n = int(input("Enter the number of terms: "))
                if n <= 0:
                    print("❌ Please enter a positive integer!")
                    continue

                if choice == "1":
                    print("\n📜 Recursive Fibonacci Sequence:")
                    print(fibonacci_recursive(n))
                elif choice == "2":
                    print("\n⚡ Iterative Fibonacci Sequence:")
                    print(fibonacci_iterative(n))
                elif choice == "3":
                    print("\n🧠 Memoization Fibonacci Sequence:")
                    print([fibonacci_memoization(i) for i in range(n)])
                elif choice == "4":
                    print("\n🔄 Generator Fibonacci Sequence:")
                    print(list(fibonacci_generator(n)))
                elif choice == "5":
                    print("\n🎨 Fibonacci Pattern:")
                    fibonacci_pattern(n)

            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        elif choice == "6":
            print("👋 Exiting... Stay curious!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
