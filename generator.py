import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def generator(length=8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    print(random_password)

generator() # Length will default to 8 if nothing is put in the call ()
