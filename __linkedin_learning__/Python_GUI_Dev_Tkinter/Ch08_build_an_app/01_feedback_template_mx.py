#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):    
        
        master.title("Explore California Feedback")
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        # Style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text='Thanks for Exploring', style='Header.TLabel').grid(row=0, column=1)
        ttk.Label(self.frame_header, wraplength=300, 
                text=("We'are glad you chose Explore California for your recent adventure. "
                    "Please tell us what you thought about the 'Desert To Sea' tour.")).grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        # self.entry_name = ttk.Entry(self.frame_content, width=24)
        # self.entry_email = ttk.Entry(self.frame_content, width=24)
        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        print(self.entry_name)
        self.text_comments = Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        self.entry_name.grid(row=1, column=0, padx=5, sticky='w') 
        self.entry_email.grid(row=1, column=1, padx=5, sticky='w')
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear', command=self.clear).grid(row=4, column=1, padx=5, sticky='w')

    def submit(self):
        print(f"Name: {self.entry_name.get()}")
        print(f"Email: {self.entry_email.get()}")
        print(f"Comments: {self.text_comments.get(1.0, 'end')}")    
        self.clear()
        messagebox.showinfo(title="Explore California Feedback", 
                message="Commnents submitted. Thank you for your feedback.")

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
