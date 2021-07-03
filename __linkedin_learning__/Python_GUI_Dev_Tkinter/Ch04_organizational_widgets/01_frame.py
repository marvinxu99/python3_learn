#!/usr/bin/python3
# frame.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.title("The Main Window")
root.config(padx=20, pady=20)

frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE)

ttk.Button(frame, text = 'Click Me').grid()

frame.config(padding = (30, 15))

myFrame = ttk.LabelFrame(root, height=100, width=200, text='My Frame')
myFrame.pack()
'''Cannot use relief for LabelFrame'''

root.mainloop()
