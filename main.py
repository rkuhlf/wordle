import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from cProfile import label
from tkinter import *
import tkinter as tk
import random

root = tk.Tk()
root.wm_geometry('320x480')
root.title('Wordle')
word_entry_guess = tk.StringVar()

with open ("realwords.csv", 'r') as file:
    textfile = file.read()
    words = list(textfile.split())
    correct_word = list(random.choice(words))

with open ('allwords.csv', 'r') as file:
    textfile = file.read()
    words = list(textfile.split())
    comparison_word = list(random.choice(words))

def word_check():
    if list(word_entry_guess.get().upper()) != "".join(correct_word).upper():
        print(correct_word)
    # word_entry = Entry(root, textvariable=word_list[x]).pack()
    # enter_word = Button(text='Enter', command = lambda: [enter_word.pack_forget(), word_check()])
    # enter_word.pack()

word_entry = Entry(root, textvariable=word_entry_guess).pack()

enter_word = Button(root, text='Enter', command = lambda: [word_check(), ])
enter_word.pack()

root.mainloop()
