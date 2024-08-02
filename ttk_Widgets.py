import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('500x500')

label1 = tk.Label(root, text="Hello World", bg="blue")
label1.pack()

label2 = ttk.Label(root, text="Label2",)
label2.pack()


root.mainloop()
#ttk widgets implementiert das Erscheinungsbild der Widgets