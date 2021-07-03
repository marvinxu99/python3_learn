#!/usr/bin/python3
# mouse.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

def mouse_press(event):
    global prev
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num)) 
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}\n'.format(event.y_root))
    prev = event

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event
    
root = Tk()

canvas = Canvas(root, width=640, height=480, background='white')
# canvas.pack()
canvas.pack(fill=BOTH, expand=True)

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()

"""
Mouse Events: Click-Related
<Button>, <ButtonPress>   : Any button was pressed
<BUtton-1>, <ButtonPress-1>  : Button 1 was pressed
<ButtonRelease-1>  : Button 1 was released
<Double-Button-1>, <Triple-Button-1)  : Button 1 was double- or triple-clicked.

Mouse Events: Movement-Related
<Enter>  : Mouse enteed widget area
<Leave>  : Mouse left widget area.
<Motion>  : Mourse was moved
<B1-Motion>  : Mouse was moved with BUtton 1 held down.
"""
