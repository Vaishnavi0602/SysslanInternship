import os
import shutil

# Enter the folder path to organize
folder_path = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

try:
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
    else:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            # Get file extension
            extension = os.path.splitext(file)[1].lower()

            folder_name = "Others"

            for category, extensions in file_types.items():
                if extension in extensions:
                    folder_name = category
                    break

            destination = os.path.join(folder_path, folder_name)

            # Create folder if it doesn't exist
            os.makedirs(destination, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(destination, file))

        print("Files organized successfully!")

except Exception as e:
    print("Error:", e)
input("\nPress Enter to exit...")
