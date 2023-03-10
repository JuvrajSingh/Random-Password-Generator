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

characterTypes = {
    "uppercaseLetter": string.ascii_uppercase,
    "lowercaseLetter": string.ascii_lowercase,
    "digit": string.digits,
    "symbol": string.punctuation
}

def generateCharacter(characterType):
    """
    Generates a random character given the type
    """
    characterChoices = characterTypes[characterType]
    character = random.choice(characterChoices)
    return character