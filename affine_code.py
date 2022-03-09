import string

cap_letters = string.ascii_uppercase
tin_letters = string.ascii_lowercase


def inv(n, base=26):
    """This function is set to get the inverse of n in a certain base"""
    for i in range(1, base):
        if (n * i) % base == 1:
            return i


def cipher(text, a, b):
    _text = ''
    for char in text:
        if char in cap_letters:
            _text += cap_letters[(a * cap_letters.index(char) + b) % 26]
        elif char in tin_letters:
            _text += tin_letters[(a * tin_letters.index(char) + b) % 26]
        else:
            _text += char
    return _text


def decipher(text, a, b):
    _text = ''
    _a = inv(a)
    _b = (-_a * b) % 26
    _text = cipher(text, _a, _b)
    return _text
