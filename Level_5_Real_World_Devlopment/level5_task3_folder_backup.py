import os
import shutil

source = input("Enter source folder path: ")
destination = input("Enter backup folder path: ")

try:
    shutil.copytree(source, destination)

    print("Backup completed successfully!")

except FileExistsError:
    print("Destination folder already exists.")

except FileNotFoundError:
    print("Source folder not found.")

except Exception as e:
    print("Error:", e)
input("\nPress Enter to exit...")