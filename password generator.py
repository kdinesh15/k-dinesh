import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

while True:
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
            break
    except ValueError:
        print("Please enter a valid number.")
