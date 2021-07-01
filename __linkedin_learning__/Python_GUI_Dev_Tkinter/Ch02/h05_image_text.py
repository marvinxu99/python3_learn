#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

        ttk.Button(master, text = "Change Text",
                   command = self.handle_change_text).grid(row = 2, column = 0)

        self.btn3 = ttk.Button(master, text = "Show Image", command = self.handle_image)
        self.btn3.grid(row = 2, column = 2)

        self.label2 = ttk.Label(master, 
                text='Hello, Tkinter. It has been a while since we last met. Great to see you again!',
                wraplength=150,
                justify=CENTER,
                font={'Courier', 12, 'bold'}
            )
        self.label2.grid(row=2, column=1)

        self.logo = PhotoImage(file='D:/dev/1_django/1_django_pg/1_django_pg_dev_multi/static/img/winter_logo.png')


    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

    def handle_change_text(self):
        """label.config(foregroud='blue', background='yellow')
        """
        if self.label2['foreground']: 
            self.label2.config(foreground='',  background='')
        else:
            self.label2.config(foreground='blue', background='yellow')

        # print(self.label2.config())

    def handle_image(self):
            self.label2.config(image=self.logo, compound='center')

def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
