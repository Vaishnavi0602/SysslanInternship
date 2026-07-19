text = input("Enter some text: ")

character_count = len(text)

words = text.split()
word_count = len(words)

print("\nText Analysis")
print("-------------")
print("Total Characters:", character_count)
print("Total Words:", word_count)
input("\nPress Enter to exit...")