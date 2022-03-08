import string

def cipher(txt, word):
    """We are in base 26 (English alphabets).
    This function is set to cipher your text through the
    key that's a simple word"""
    txt = txt.upper()
    word = word.upper()
    upper_letters = string.ascii_uppercase
    encrypted_txt = ''
    j = 0
    for i in range(len(txt)):
        if txt[i].isupper():
            encrypted_txt += upper_letters[(upper_letters.index(txt[i]) + upper_letters.find(word[j])) % 26]
            j += 1
        else:
            encrypted_txt += txt[i]
        if j == len(word):
            j = 0
    return encrypted_txt

"""def decipher(txt, word):
        #We can decipher an encrypted text by ciphering it twenty-six times
        for i in range(25):
            txt = cipher(txt, word)
    return txt"""

def decipher(txt, word):
    txt = txt.upper()
    word = word.upper()
    upper_letters = string.ascii_uppercase
    decrypted_txt = ''
    j = 0
    for i in range(len(txt)):
        if txt[i].isupper():
            decrypted_txt += upper_letters[(upper_letters.index(txt[i]) - upper_letters.find(word[j])) % 26]
            j += 1
        else:
            decrypted_txt += txt[i]
        if j == len(word):
            j = 0
    return decrypted_txt

#print(decipher(cipher("CETTEPHRASENEVEUTRIENDIRE", 'RIDE'), 'RIDE'))
    
    
