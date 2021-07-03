#!/usr/bin/python3
# dialogs.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import filedialog

filename = filedialog.askopenfile()
print(filename.name)

"""
askdirectory()
asksaveasfile(mode)
asksaveasfilename()

askopenfile(mode)
askopenfiles(mode)
askopenfilename()
askopenfilenames()
"""