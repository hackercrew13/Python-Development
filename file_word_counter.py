import re
import collections
import csv

def count_word_frequencies(filename):
    """Reads a text file and counts occurrences of each word, sorting alphabetically."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()  # Convert to lowercase for case-insensitive counting

        # Remove punctuation and split into words
        words = re.findall(r"\b[a-zA-Z0-9']+\b", text)

        # Count word occurrences
        word_counts = collections.Counter(words)

        # Sort words alphabetically
        sorted_word_counts = dict(sorted(word_counts.items()))

        return sorted_word_counts

    except FileNotFoundError:
        print("❌ Error: File not found!")
        return None

def save_to_csv(word_counts, output_filename="word_frequencies.csv"):
    """Saves the word frequency counts to a CSV file."""
    try:
        with open(output_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "Count"])  # Header row
            for word, count in word_counts.items():
                writer.writerow([word, count])

        print(f"✅ Word frequencies saved to {output_filename}")
    except Exception as e:
        print(f"❌ Error saving CSV: {e}")

def main():
    """Main function to execute file word counting."""
    filename = input("📂 Enter the filename (with extension): ").strip()

    word_counts = count_word_frequencies(filename)

    if word_counts:
        print("\n🔎 Word Frequency Count (Sorted Alphabetically):")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

        save_to_csv(word_counts)

if __name__ == "__main__":
    main()
