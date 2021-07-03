#!/usr/bin/python3
# grid.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 1, column = 1, sticky='nsew')
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0)
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1, sticky='nsew')

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.columnconfigure(1, weight = 1)

root.mainloop()
