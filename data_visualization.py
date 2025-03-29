import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(file_path):
    """Loads a dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("\n✅ Dataset Loaded Successfully!\n")
        print(df.head())  # Display first 5 rows
        return df
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def plot_visualization(df):
    """Generates different types of visualizations based on user choice."""
    print("\n📊 Choose a Visualization Type:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Scatter Plot")
    print("4. Histogram")
    print("5. Heatmap (for correlation)")

    choice = input("Enter the number of the visualization: ").strip()

    if choice == "1":
        x_col = input("Enter the column for X-axis: ").strip()
        y_col = input("Enter the column for Y-axis: ").strip()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=df[x_col], y=df[y_col])
        plt.title(f"Bar Chart of {y_col} vs {x_col}")
    
    elif choice == "2":
        x_col = input("Enter the column for X-axis: ").strip()
        y_col = input("Enter the column for Y-axis: ").strip()
        plt.figure(figsize=(8, 5))
        sns.lineplot(x=df[x_col], y=df[y_col])
        plt.title(f"Line Chart of {y_col} vs {x_col}")

    elif choice == "3":
        x_col = input("Enter the column for X-axis: ").strip()
        y_col = input("Enter the column for Y-axis: ").strip()
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df[x_col], y=df[y_col])
        plt.title(f"Scatter Plot of {y_col} vs {x_col}")

    elif choice == "4":
        col = input("Enter the column for Histogram: ").strip()
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, bins=20)
        plt.title(f"Histogram of {col}")

    elif choice == "5":
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Heatmap of Correlations")

    else:
        print("❌ Invalid choice! Please restart the program.")
        return

    plt.show()

def main():
    """Main function to load dataset and generate visualizations."""
    file_path = input("📂 Enter the CSV filename (e.g., data.csv): ").strip()
    
    df = load_dataset(file_path)
    if df is not None:
        plot_visualization(df)

if __name__ == "__main__":
    main()
