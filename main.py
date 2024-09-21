import random
import string
import json


def generate_password(length=8,
                      use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on specified criteria.

    Parameters:
    length (int): The desired length of the password (default(8)).
    use_uppercase (bool): Whether to include uppercase letters (default(True)).
    use_numbers (bool): Whether to include numbers (default(True)).
    use_symbols (bool): Whether to include special characters (default(True)).

    Returns:
    str: A randomly generated password.

    Raises:
    ValueError: If no character sets are selected or if the length exceeds
                the number of unique characters available.
    """
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all chosen character sets
    all_chars = lowercase + uppercase + numbers + symbols

    if not all_chars:
        raise ValueError(
            "You must include at least one character set for the password!")

    # Check if it's possible to generate a password with no repeated characters
    if length > len(all_chars):
        raise ValueError(
            "Length exceeds the number of unique characters available!")

    # Generate the password
    password = ''.join(random.sample(all_chars, length))

    return password


with open("./information.json", "r") as file:
    data = json.load(file)
password = generate_password(length=data['length'],
                             use_uppercase=data['use_uppercase'],
                             use_numbers=data['use_numbers'],
                             use_symbols=data['use_symbols'])
print(f"Generated password: {password}")
