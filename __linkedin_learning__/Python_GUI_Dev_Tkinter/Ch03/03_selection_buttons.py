#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()


checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
checkbutton.pack()

"""
tkinter variable classes:
- BooleanVar
- DoubleVar
- IntVar
- StringVar
"""
spam = StringVar()
# spam.set('SPAM!')
# print(spam.get())

checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')

def checkbutton_state():
	print('selected:', checkbutton.instate(['selected']))
	print(spam.get())

checkbutton.config(command=checkbutton_state)

# Widget state
checkbutton.state(['disabled'])    # This is to disable the button
print('disabled:', checkbutton.instate(['disabled']))
checkbutton.state(['!disabled'])   # This is to enable the button
print('!disabled:', checkbutton.instate(['!disabled']))


breakfast = StringVar()
breakfast.set('Initial value')

def check_radiobutton():
	print('radio checked:', breakfast.get())

ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		command=check_radiobutton,
		value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		command=check_radiobutton,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		command=check_radiobutton,
		value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		command=check_radiobutton,
		value = 'SPAM').pack()

print(breakfast.get()) 	# Note: value will be empty if no selection is made

checkbutton.config(textvariable = breakfast)

root.mainloop()
