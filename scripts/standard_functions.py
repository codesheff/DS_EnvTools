#!/usr/bin/env python3


def genpassword(forbidden_chars={'!* '}, passwordLength=8):

    """
    This function will generate a random password

    Password will be generated at random from all printable characters.
    Parameters: 
         forbidden_chars:  Characters that are not allowed in the password
         passwordLenght:   Length of the password to be generated
    """

    import random
    import string

    characters=set(string.printable)

    for character in forbidden_chars:
        characters.discard(character)

    str_characters=''.join(characters)

    new_password = ''.join(random.choice(str_characters) for i in range(passwordLength))

    print(forbidden_chars)
    print(str(passwordLength))

    return new_password



#print(genpassword('testchars'))
#print(genpassword(passwordLength=15, forbidden_chars=r'xedr'))