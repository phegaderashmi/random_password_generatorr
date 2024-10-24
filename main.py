import random
import string

def generate_password(length, use_digits=True, use_special=True, use_upper=True):
    """
    Generate a random password.

    :param length: Length of the password
    :param use_digits: Whether to include digits
    :param use_special: Whether to include special characters
    :param use_upper: Whether to include uppercase letters
    :return: Randomly generated password
    """

    # Define character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special else ""

    # Combine all characters based on user preferences
    all_chars = lower_chars + upper_chars + digits + special_chars

    # Ensure that we have at least one type of character
    if not all_chars:
        raise ValueError("At least one character set must be selected")

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    # User input for password length and options
    length = int(input("Enter the length of the password: "))
    
    # Optional customization for password characteristics
    use_digits = input("Include digits (0-9)? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters (!@#$%^&*)? (yes/no): ").lower() == 'yes'
    use_upper = input("Include uppercase letters (A-Z)? (yes/no): ").lower() == 'yes'

    # Generate and print password
    password = generate_password(length, use_digits, use_special, use_upper)
    print(f"Generated password: {password}")
