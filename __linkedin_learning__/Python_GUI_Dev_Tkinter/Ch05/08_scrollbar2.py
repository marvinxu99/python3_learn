#!/usr/bin/python3
# scrollbar.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# text = Text(root, width=40, height=10, wrap='word')
text = Text(root, width=40, height=10, wrap=NONE)    # Must use NONE instead of None
text.grid(row=0, column=0)

xscrollbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=text.xview)
xscrollbar.grid(row=2, column=0, sticky='ew')

yscrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
yscrollbar.grid(row=0, column=1, sticky='ns')

text.config(xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set)
# text.config(yscrollcommand = yscrollbar.set)

# canvas.grid(row = 1, column = 0)
# xscroll.grid(row = 2, column = 0, sticky = 'ew')

# def canvas_click(event):
#     x = canvas.canvasx(event.x)
#     y = canvas.canvasy(event.y)
#     canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

# canvas.bind('<1>', canvas_click)

root.mainloop()
