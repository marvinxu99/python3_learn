#!/usr/bin/python3
# toplevel.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *      
    
root = Tk()

window = Toplevel(root)
window.title('New Window')

window.lower()
window.lift(root)

window.state('zoomed')      # Maximizw the window
window.state('withdrawn')   # hide the window
window.state('iconic')      # Minimize the window
window.state('normal')      # de-iconified 
print(window.state())       # ==> zoomed
window.state('normal')

window.iconify()
window.deiconify()

window.geometry('640x480+50+100')   # WIDTHxHEIGHT+X+Y
print(window.geometry())
window.resizable(False, False)
window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True, True)

root.destroy()

root.mainloop()
