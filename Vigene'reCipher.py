from itertools import cycle
LEN = 127


def full_encode(value, keys):
    """Function to encrypt using the Vigenere"""
    return ''.join(map(lambda x: chr((ord(x[0]) + ord(x[1])) % LEN), zip(value, cycle(keys))))


def full_decode(value, keys):
    """Function to decrypt using the Vigenere"""
    return ''.join(map(lambda x: chr((ord(x[0]) - ord(x[1])) % LEN), zip(value, cycle(keys))))


if True:
    key = str(input('Enter key: '))
    word = str(input('Enter the word, which you want to encrypt: '))
    cipher = full_encode(word, key)
    print('cipher:', cipher)
    decoded = full_decode(cipher, key)
    print('Word:', decoded)