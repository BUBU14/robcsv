import io
from check import checkFile
from create import createFile
from tkinter import *

fenetre = Tk()



#Frame
F_choice = Frame(fenetre, bg="white", borderwidth=2, relief=GROOVE)
F_verify = Frame(F_choice, borderwidth=2, relief=GROOVE)
F_Create = Frame(F_choice, borderwidth=2, relief=GROOVE)


#Label
L_titre = Label(fenetre, text="Gestion fichier csv")

#Button
B_verify = Button(F_verify, text="verifier")
B_create = Button(F_Create, text="generer")
B_close = Button(fenetre, text="fermer", command=fenetre.quit)



#Generation Graphique

L_titre.pack()
F_verify.pack(side=LEFT, padx=30, pady=30)
B_verify.bind("<Button-1>",checkFile)
B_verify.pack()
F_Create.pack(side=RIGHT, padx=30, pady=30)
F_choice.pack()
B_create.bind("<Button-1>",createFile)
B_create.pack()
B_close.pack()

#Fenetre
fenetre.mainloop()


