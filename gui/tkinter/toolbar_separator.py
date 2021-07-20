import tkinter as tk
from tkinter import ttk

root = tk.Tk()
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x", padx=20, pady=20)

button1 = tk.Button(toolbar, text="Home")
button2 = tk.Button(toolbar, text="Insert")
sep = ttk.Separator(toolbar)

button1.pack(side="left")
sep.pack(side="left", fill="y", padx=4, pady=4)
button2.pack(side="left")

root.mainloop()