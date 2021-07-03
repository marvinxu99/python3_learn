#!/usr/bin/python3
# dialogs.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import messagebox

"""
Informational message box:
- showinfo()
- showwarning()
- showerror()
"""
messagebox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')

"""Questions
- askyesno()
- askokcancel()
- askretrycancel()
- askyesnocancel()
- askquestion()

"""
print(messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?'))

