import random
import string

"""
Generate a random password 8 characters long everytime the programme is run
Password will include:
    2 uppercase letters
    2 lowercase letters
    2 digits
    2 symbols
These characters will appear in a random order
"""

character_types = {
    "uppercase_letter": string.ascii_uppercase,
    "lowercase_letter": string.ascii_lowercase,
    "digit": string.digits,
    "symbol": string.punctuation
}

def generate_character(character_type):
    """
    Generates a random character given the type
    """
    character_choices = character_types[character_type]
    character = random.choice(character_choices)
    return character

def shuffle_characters(characters):
    """
    Given a string, returns a string with all the characters shuffled
    """
    shuffled_characters = "".join(random.sample(characters, len(characters)))
    return shuffled_characters

def generate_password():
    """
    Generates a random password
    """
    password = ""
    password += generate_character("uppercase_letter")
    password += generate_character("uppercase_letter")
    password += generate_character("lowercase_letter")
    password += generate_character("lowercase_letter")
    password += generate_character("digit")
    password += generate_character("digit")
    password += generate_character("symbol")
    password += generate_character("symbol")

    final_password = shuffle_characters(password)

    return final_password


if __name__ == "__main__":
    password = generate_password()
    print(password)