def validate_email(email):
    if "@" not in email:
        return False

    if email.count("@") != 1:
        return False

    if "." not in email:
        return False

    at_pos = email.index("@")

    if at_pos == 0:
        return False

    if at_pos == len(email) - 1:
        return False

    return True


email = input("Enter an email address: ")

if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
input("\nPress Enter to exit...")