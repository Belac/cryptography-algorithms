import string

cap_letters = string.ascii_uppercase
tin_letters = string.ascii_lowercase


def cipher(text, word):
    _text = ''
    word = word.upper()
    j = 0
    for i in range(len(text)):
        if text[i] in cap_letters:
            _text += cap_letters[(cap_letters.index(text[i]) + cap_letters.find(word[j])) % 26]
            j += 1
        elif text[i] in tin_letters:
            _text += tin_letters[(tin_letters.index(text[i]) + cap_letters.find(word[j])) % 26]
            j += 1
        else:
            _text += text[i]
        j %= len(word)
    return _text


def decipher(text, word):
    _text = ''
    word = word.upper()
    j = 0
    for i in range(len(text)):
        if text[i] in cap_letters:
            _text += cap_letters[(cap_letters.index(text[i]) - cap_letters.find(word[j])) % 26]
            j += 1
        elif text[i] in tin_letters:
            _text += tin_letters[(tin_letters.index(text[i]) - cap_letters.find(word[j])) % 26]
            j += 1
        else:
            _text += text[i]
        j %= len(word)
    return _text
