#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

def callback():
    print('Clicked!')

# command
button.config(command = callback)
button.invoke()   # this is to simulate the button is clicked

# Widget state
button.state(['disabled'])    # This is to disable the button
print(button.instate(['disabled']))
button.state(['!disabled'])   # This is to enable the button
print(button.instate(['!disabled']))

logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
button.config(image = logo, compound = LEFT)
small_logo = logo.subsample(5, 5)
button.config(image = small_logo)

root.mainloop()
