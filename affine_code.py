from math import gcd
import string

def phi(n):
    value = 0
    for i in range(1, n):
        value += gcd(i, n) == 1
    return value

def cipher(txt, a, b):
    txt = txt.upper()
    letters = string.ascii_uppercase
    _txt = ''
    for char in txt:
        if char.isalpha():
            _txt += letters[(a * letters.index(char) + b) % 26]
        else:
            _txt += char
    return _txt

def decipher(txt, a, b):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            a = i
            b *= -a
            break
    return cipher(txt, a, b)

print(decipher(cipher("Here we are!", 7, 10), 7, 10))
