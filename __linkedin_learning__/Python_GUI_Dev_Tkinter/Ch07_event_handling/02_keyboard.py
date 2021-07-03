#!/usr/bin/python3
# keyboard.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

""" Callbacks vs Events
- Callbacks only available for specific actions
- Tkinter can bind to events with specific handlers
- There's a wide variety of event handlers
"""

# https://www.tcl.tk/man/tcl8.4/TkCmd/bind.html#M11  
""" Tk Event Types (frequently used)
- ButtonPress, ButtonRelease, Motion
- Enter, Leave
- KeyPress, KeyRelease
- FocusIn, FocusOut
"""

from tkinter import *
from tkinter import ttk        

def key_press(event):
    # print('type: {}'.format(event.type))
    # print('widget: {}'.format(event.widget))
    # print('char: {}'.format(event.char))
    # print('keysym: {}'.format(event.keysym))
    # print('keycode: {}\n'.format(event.keycode))
    print(f'type: {event.type}, widget: {event.widget}, char: {event.char}, keysym: {event.keysym}, keycode: {event.keycode}')

"""
type: 2, widget: ., char: , keysym: XF86AudioMute, keycode: 173
type: 2, widget: ., char: d, keysym: d, keycode: 68

*** event type 2 - meaning it is KeyPress event.
"""

def shortcut(action):
    print(action)
    
root = Tk()

root.bind('<KeyPress>', key_press)
#root.bind('<Key>', key_press)

root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.bind('<KeyPress-Delete>', lambda e: shortcut('Delete'))
root.bind('<KeyPress-Insert>', lambda e: shortcut('Insert'))

root.bind('<a>', lambda e: shortcut('a'))
root.bind('<A>', lambda e: shortcut('A'))

root.bind('<Control-Alt-Next>', lambda e: shortcut('Ctrl+Alt+Page Down'))

"""
<Key>, <KeyPress>  : User pressed any key
<KeyPress-Delete>  : User pressed Delete key
<KeyRelease-Right> : User release Right Arrow key

a,b,c,1,2,3, etc... and <space>, <less>  : user pressed a "printable" key

<Shift_L>, <Control-R>, <F5>, <Up>  : User pressed a "special" key. 

<Return>  : user pressed the Enter key.
<Control-Alt-Next>  : user pressed Ctrl+Alt+Page Down keys

"""

root.mainloop()
