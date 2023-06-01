import string

# To get all the uppercase | lowercase characters
cap_letters = string.ascii_uppercase
tin_letters = string.ascii_lowercase


def cipher(word):
    """
    Considering β the alphabetical order of each alpha letter contained
    in a word, the formula to cipher this letter is :
    β + 25 - 2 * d(A, β) or β + 25 - 2 * d(a, β)
    """
    _word = ''
    for char in word:
        if char in cap_letters:
            _word += chr(ord(char) + 25 - (2 * (ord(char) - ord('A'))))
        elif char in tin_letters:
            _word += chr(ord(char) + 25 - (2 * (ord(char) - ord('a'))))
        else:
            _word += char
    return _word


def decipher(word):
    # To decrypt, just encrypt again
    return cipher(word)
