import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Code_Files": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

def organize_files(directory):
    """Scans and organizes files in the specified directory."""
    if not os.path.exists(directory):
        print(f"❌ Error: The directory '{directory}' does not exist.")
        return
    
    # Create subfolders if they don't exist
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Iterate through files and move them to the appropriate folder
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files to their respective folders
        file_ext = os.path.splitext(filename)[-1].lower()
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                dest_folder = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"📂 Moved: {filename} → {category}/")
                moved = True
                break
        
        # If file type is unknown, move it to "Others"
        if not moved:
            other_folder = os.path.join(directory, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"📂 Moved: {filename} → Others/")

    print("\n✅ File organization completed successfully!")

def main():
    """Main function to execute file organization."""
    target_directory = input("📁 Enter the folder path to organize: ").strip()
    organize_files(target_directory)

if __name__ == "__main__":
    main()
