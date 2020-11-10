import string
import random
import pyperclip

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def generator(length=8, save_to_file='y'):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)

    pyperclip.copy(random_password)
    print(f'{random_password} Has been copied to your clipboard!')
    if save_to_file == 'y':
        print(f'{random_password} Has been logged to the logs.txt file!')
        log = open("logs.txt", "a")
        log.write(f'{random_password}\n')
        log.close()
    elif save_to_file == 'n':
        print("Your password haven't been logged!")
    else:
        print("I don't know what you're trying to do.")


def user_input(length=8):
    try:
        chars = int(input("How many characters do you want your password to be?: "))
        length = chars or length
    except ValueError:
        user_input(length=length)

    save_to_file = input("Do you want to log generated password to log.txt? (y/n): ")

    if not save_to_file == 'y' and not save_to_file == 'n':
        print("Invalid input please try again.")
        user_input(length=length)

    return length, save_to_file


length, save_to_file = user_input()
generator(length, save_to_file)
