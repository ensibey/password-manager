import random
import string

def generate_random_password(length, include_letters=True, include_digits=True, include_special_characters=True):
    characters = ''

    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    random_password = ''.join(random.choice(characters) for i in range(length))
    return random_password

def save_password(password_name, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{password_name}: {password}\n")
    print("Password successfully saved.")

def main():
    password_name = input("Enter the name for the password: ")
    length = int(input("Enter the length of the password to generate: "))
    include_letters = input("Include letters? (Type 'y' or 'Y' for Yes, any other character for No): ").lower() == 'y'
    include_digits = input("Include digits? (Type 'y' or 'Y' for Yes, any other character for No): ").lower() == 'y'
    include_special_characters = input("Include special characters? (Type 'y' or 'Y' for Yes, any other character for No): ").lower() == 'y'

    try:
        password = generate_random_password(length, include_letters, include_digits, include_special_characters)
        print("Generated password:", password)
        save_password(password_name, password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
