import random
import string

"""
Generate a random password 8 characters long everytime the programme is run
"""

character_types = {
    "uppercase letter": string.ascii_uppercase,
    "lowercase letter": string.ascii_lowercase,
    "digit": string.digits,
    "symbol": string.punctuation,
    "any": string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
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

def generate_password(length=8, uppercase=2, lowercase=2, digits=2, symbols=2):
    """
    Generates a random password given:
    Length of the password
    How many uppercase letters it should contain
    How many lowercase letters it should contain
    How many digits it should contain
    How many symbols it should contain
    """
    password = ""
    for i in range(uppercase):
        password += generate_character("uppercase letter")
    for j in range(lowercase):
        password += generate_character("lowercase letter")
    for k in range(digits):
        password += generate_character("digit")
    for l in range(symbols):
        password += generate_character("symbol")

    remaining = length - (uppercase + lowercase + digits + symbols)
    if remaining > 0:
        for m in range(remaining):
            password += generate_character("any")

    final_password = shuffle_characters(password)

    return final_password