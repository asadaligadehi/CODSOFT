import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Combine character sets based on complexity
    if length < 4:
        print("Password length is too short. Please choose a longer length.")
        return

    if length < 8:
        char_set = lowercase_letters + digits
    elif length < 12:
        char_set = lowercase_letters + uppercase_letters + digits
    else:
        char_set = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))

    password = generate_password(length)

    if password:
        print("Generated Password: " + password)
    else:
        print("Password generation failed.")

if __name__ == "__main__":
    main()
