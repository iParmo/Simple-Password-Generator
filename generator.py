import string
import random
import pyperclip

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def generator(length=8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)


    try:
        chars = int(input("How many characters do you want your password to be?: "))
        length = chars or length
    except ValueError:
        pass

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)


    pyperclip.copy(random_password)
    print(f'{random_password} Has been copied to your clipboard!')
    yes = input("Do you want to log generated password to log.txt? (y/n): ")
    if yes == 'y':
        print(f'{random_password} Has been logged to the logs.txt file!')
        log = open("logs.txt", "a")
        log.write(f'{random_password}\n')
        log.close()
    elif yes == 'n':
        print("Your password haven't been logged!")
    else:
        print("Invalid input please try again.")
        generator()

generator()
# Length will default to 8 if nothing is put in the call ()
