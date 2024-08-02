import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('500x500')

label1 = tk.Label(root, text="Hello World", bg="blue")
label1.pack()


image = Image.open('IMG_0046.PNG').resize((300, 500))   #Foto Image eingefügt und größe angepasst
photo = ImageTk.PhotoImage(image)
label2 = tk.Label(root, image=photo)
label2.pack()





root.mainloop()
#ttk widgets implementiert das Erscheinungsbild der Widgets

#Konfiguration von ttk widgets mit der .configure methode
