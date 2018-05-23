from tkinter import FLAT, GROOVE, SUNKEN, RIGHT
from tkinter import Frame, Button, Tk, Label, Spinbox

root = Tk()

# Class for create new bow plan
class createPlan:
    X_product = 0
    Y_product = 0
    X_box = 0
    Y_box = 0
    layerProduct_X = 0
    layerProduct_Y = 0
    nbrProduct = 0
    halfLayer = 0

def createFile(plan):
    print(plan)
    print("I'm create file")


# Get information for box plan
def getInfo(event):
    plan = createPlan
    plan.X_product = int(SB_xProduct.get())
    plan.Y_product = int(SB_yProduct.get())
    plan.X_box = int(SB_xBox.get())
    plan.Y_box = int(SB_yBox.get())
    plan.layerProduct_X = int(SB_xLayerProduct.get())
    plan.layerProduct_Y = int(SB_xLayerProduct.get())
    plan.nbrProduct = int(SB_nbrProduct.get())
    plan.halfLayer = int(SB_halfLayer.get())
    createFile(plan)


# Frame
F_choice = Frame(root, bg="white", borderwidth=2, relief=FLAT)
F_create = Frame(F_choice, borderwidth=2, relief=SUNKEN)
F_product = Frame(F_create, borderwidth=2, relief=SUNKEN)
F_box = Frame(F_create,  borderwidth=2, relief=GROOVE)
F_layerProduct = Frame(F_create,  borderwidth=2, relief=GROOVE)
F_nbrProduct = Frame(F_create, borderwidth=2, relief=GROOVE)
F_halfLayer = Frame(F_create,  borderwidth=2, relief=GROOVE)

# Spinbox
SB_xProduct = Spinbox(F_product, from_=0, to=1000)
SB_yProduct = Spinbox(F_product, from_=0, to=1000)
SB_xBox = Spinbox(F_box, from_=0, to=1000)
SB_yBox = Spinbox(F_box, from_=0, to=1000)
SB_xLayerProduct = Spinbox(F_layerProduct, from_=0, to=1000)
SB_yLayerProduct = Spinbox(F_layerProduct, from_=0, to=1000)
SB_nbrProduct = Spinbox(F_nbrProduct, from_=0, to=1000)
SB_halfLayer = Spinbox(F_halfLayer, from_=0, to=1000)


# Label
L_titre = Label(root, text="Gestion fichier csv")
L_product = Label(F_product, text="Produit : ")
L_box = Label(F_box, text="Carton : ")
L_layerProduct = Label(F_layerProduct, text="Nombre prod/car : ")
L_nbrProduct = Label(F_nbrProduct, text="Nombre total de prduit : ")
L_halfLayer = Label(F_halfLayer, text="Nombre de sous-couche")

L_xProduct = Label(F_product, text="X:")
L_yProduct = Label(F_product, text="Y:")
L_xBox = Label(F_box, text="X:")
L_yBox = Label(F_box, text="Y:")
L_xLayerProduct = Label(F_layerProduct, text="X:")
L_yLayerProduct = Label(F_layerProduct, text="Y:")


# Button
B_create = Button(F_create, text="generer")
B_close = Button(root, text="fermer", command=root.quit)

# Generation Graphique
L_titre.pack()

F_product.pack()
L_product.pack()
L_xProduct.pack()
SB_xProduct.pack()
L_yProduct.pack()
SB_yProduct.pack()

F_box.pack()
L_box.pack()
L_xBox.pack()
SB_xBox.pack()
L_yBox.pack()
SB_yBox.pack()

F_layerProduct.pack()
L_layerProduct.pack()
L_xLayerProduct.pack()
SB_xLayerProduct.pack()
L_yLayerProduct.pack()
SB_yLayerProduct.pack()

F_nbrProduct.pack()
L_nbrProduct.pack()
SB_nbrProduct.pack()

F_halfLayer.pack()
L_halfLayer.pack()
SB_halfLayer.pack()

F_create.pack(side=RIGHT, padx=30, pady=30)
B_create.bind("<Button-1>", getInfo)
B_create.pack()

F_choice.pack()

B_close.pack()

#Fenetre
root.mainloop()


