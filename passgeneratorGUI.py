import random
import string
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *

import pyperclip
from ttkthemes import ThemedTk

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

window = ThemedTk(theme='arc')

txt = Entry(window, width=5)
chk_state = BooleanVar()
chk_state.set(False)


def clicked():
    global printable
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable)
    random.shuffle(printable)

    try:
        length = int(txt.get())
    except ValueError:
        messagebox.showerror('Error', 'Please only use numbers! Error: ValueError')
        return

    global random_password
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)

    pyperclip.copy(random_password)

    if not chk_state.get():
        messagebox.showinfo('Password Copied', 'Your password has been copied')

    if chk_state.get():
        f = filedialog.asksaveasfile(mode='a')
        f.write(f'{random_password}\n')
        f.close()
        messagebox.showinfo('Password Logged', 'Your password has been logged and copied!')


window.title("Password Generator")
window.geometry('460x90')
lbl = Label(window, text="How many characters do you want your password to be?")
lbl.grid(column=0, row=0)
btn = Button(window, text="Generate", command=clicked)
btn.grid(column=2, row=0)
txt.focus()
txt.grid(column=1, row=0)
chk = Checkbutton(window, text='log password', variable=chk_state)
chk.grid(column=2, row=1)
lbl2 = Label(window, text="When asked to replace just say yes. It won't actually replace")
lbl2.grid(column=0, row=1)
lbl3 = Label(window, text="Disclaimer: Logging your password is extremly unsafe!")
lbl3.grid(column=0, row=2)
lbl4 = Label(window, text="Your password gets saved copied automatically though")
lbl4.grid(column=0, row=4)

window.mainloop()
