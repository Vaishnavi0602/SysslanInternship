from datetime import datetime

message = input("Enter log message: ")

current_time = datetime.now()

file = open("logfile.txt", "a")

file.write(str(current_time))
file.write(" - ")
file.write(message)
file.write("\n")

file.close()

print("Log Entry Saved Successfully!")
input("\nPress Enter to exit...")