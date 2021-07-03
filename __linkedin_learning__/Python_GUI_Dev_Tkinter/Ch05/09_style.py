#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

"""
Widget States:
active, disabled, focus, pressed, selected, backgroud, readonly, 
alternate, invalid, hover
"""


from tkinter import *
from tkinter import ttk        
    
root = Tk()

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')      
button1.pack()
button2.pack()

style = ttk.Style()

# Theme
print(style.theme_names())       # what themes are available
print(style.theme_use())         # What theme is being used
style.theme_use('classic')      
style.theme_use('vista')

"""Widget Style Names
    Usually "T" + widget name. TButton, TFrame

    for Treeview is TreeView (no extra "T")
    TPanedwindow ("w" is only lowercase)
    Horizontal.RScale or Vertical.TScale
    Horizontal.TScrollbar or Vertical.TScrollbar
    Horizontal.TProgressbar or Vertical.TProgressbar
"""
print(button1.winfo_class())
style.configure('TButton', foreground = 'blue')

style.configure('Alarm.TButton', foreground = 'orange',
                font = ('Arial', 24, 'bold'))
button2.configure(style = 'Alarm.TButton')

style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')])
button2.state(['disabled'])

print(style.layout('TButton'))
"""
[('Button.button', 
  {'sticky': 'nswe', 
   'children': [('Button.focus', 
                 {'sticky': 'nswe', 
                    'children': [('Button.padding', 
                                  {'sticky': 'nswe', 
                                   'children': [('Button.label', {'sticky': 'nswe'})]})]

  Button element
  Focus element
  Padding element
  Label element

"""


print(style.element_options('Button.label'))

print(style.lookup('TButton', 'foreground'))

root.mainloop()
