import random

"""
Generate a random password 8 characters long everytime the programme is run
Password will include:
    2 uppercase letters
    2 lowercase letters
    2 digits
    2 punctuation signs
These characters will appear in a random order
"""

characterTypes = {
    "uppercaseLetter": [65, 90],
    "lowercaseLetter": [97, 122],
    "digit": [48, 57],
    "punctuationSign": [[33, 47], [58, 64], [91, 96], [123, 126]]
}

def generateCharacter(characterType):
    """
    Generates a random character given the type
    """

    asciiCodes = characterTypes[characterType]

    if isinstance(asciiCodes[0], int):
        character = chr(random.randint(asciiCodes[0], asciiCodes[1]))
    else:
        #todo
        return
    return character