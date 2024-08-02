#Grafische Oberflaeche

import tkinter as tk

root = tk.Tk()
root.title("Das ist der Titel")             #Änderung des Programmtitels
root.geometry("350x150")                    #Fenstergröße beim Starten des Programmes
root.minsize(width=250, height=250)         #Mindestgröße des Fensters
root.maxsize(width=600, height=600)         #Maximalgröße des Fensters
root.resizable(width=False, height=False)   #Sperre des Vergrößern und Verkleinern

label1 = tk.Label(root, text="Label1", bg= "blue") #Label Widget mit Text mit Hintergundfarbe blau
label1.pack(side="top", expand=True, fill="x", )         #Ausrichtung oben mit platz auf der ganzen Zeile
label2 = tk.Label(root, text="Label2", bg= "red")
label2.pack(side="top", expand=True, fill="both", ) #Ausrichtung nach unten



root.mainloop()

#Layout Manager Pack:
#Pack, Grid und Place Layout Manager
# Pack Manager positioniert die Widgets im GUI
#side Befehle: bottom, left, right, top


