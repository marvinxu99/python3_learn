from tkinter import *
from tkinter import ttk        

def startgame():

    pass

root = Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
root.option_add("*Button.Background", "black")
root.option_add("*Button.Foreground", "red")

root.title('The game')
#You can set the geometry attribute to change the root windows size
root.geometry("500x400") #You want the size of the app to be 500x500
root.resizable(0, 0) #Don't allow resizing in the x or y direction

back = ttk.Frame(root)
back.config(relief=RAISED)
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height

#Changed variables so you don't have these set to None from .pack()
go = ttk.Button(back, text='Start Game', command=startgame)
go.pack()
close = ttk.Button(back, text='Quit', command=root.destroy)
close.pack()
info = ttk.Label(back, text='Made by me!', background='red', foreground='black')
info.pack()

back.pack(fill=BOTH, expand=1) #Expand the frame to fill the root window

root.mainloop()