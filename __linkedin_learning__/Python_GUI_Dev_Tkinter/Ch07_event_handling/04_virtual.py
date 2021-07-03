#!/usr/bin/python3
# virtual.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

"""
Virtual events:

<<Copy>>  : 
"""

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

# Create a new event binding
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))

print(entry.event_info('<<OddNumber>>'))
'''('1', '3', '5', '7', '9')'''

# Generate an virtual event
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# Delete the virtual event we created
entry.event_delete('<<OddNumber>>')

root.mainloop()
