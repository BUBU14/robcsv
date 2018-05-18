import io
from os.path import basename
from check import checkFile
from create import createFile
from tkinter import Frame, Button, Listbox, Tk, Label
from tkinter import FLAT, GROOVE, SUNKEN, LEFT, RIGHT
from tkinter.filedialog import askopenfile

root = Tk()

#filepath
def getFile(event):
    filepath = askopenfile(title="Ouvrir un csv", filetypes=[('csv files','.csv'),('all files','.*')])
    Li_file.insert(1,filepath.name)

#Frame
F_choice = Frame(root, bg="white", borderwidth=2, relief=FLAT)
F_verify = Frame(F_choice, borderwidth=2, relief=GROOVE)
F_Create = Frame(F_choice, borderwidth=2, relief=SUNKEN)

#Label
L_titre = Label(root, text="Gestion fichier csv")

#Button
B_openFile = Button(F_verify, text="ouvrir")
B_verify = Button(F_verify, text="verifier")
B_create = Button(F_Create, text="generer")
B_close = Button(root, text="fermer", command=root.quit)

#Liste
Li_file = Listbox(F_verify)

#Generation Graphique

L_titre.pack()
B_openFile.bind("<Button-1>",getFile)
B_openFile.pack()
Li_file.pack()
F_verify.pack(side=LEFT, padx=30, pady=30)
B_verify.bind("<Button-1>", lambda event : checkFile(Li_file.get(Li_file.curselection()), event))
B_verify.pack()
F_Create.pack(side=RIGHT, padx=30, pady=30)
F_choice.pack()
B_create.bind("<Button-1>", createFile)
B_create.pack()
B_close.pack()

#Fenetre
root.mainloop()


