import secrets
import string


def generate_password():
    print("\n=== PASSWORD GENERATOR ===")

    try:
        length = int(input("Password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 4:
        print("Password should be at least 4 characters long.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))

    print("\nGenerated Password:")
    print(password)

    strength = check_strength(password)

    print(f"\nStrength: {strength}")


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Strong"
    else:
        return "Very Strong"


while True:
    generate_password()

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("Goodbye!")
        break
