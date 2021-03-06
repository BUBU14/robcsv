import string
from tkinter import FLAT, GROOVE, SUNKEN, RIGHT
from tkinter import Frame, Button, Tk, Label, Spinbox, Entry, StringVar
import csv
import numpy as np

root = Tk()


# Class pour recuprerer les données
class giveData:
    X_product = 0
    Y_product = 0
    Z_product = 0
    X_box = 0
    Y_box = 0
    layerProduct_X = 0
    layerProduct_Y = 0
    nbrProduct = 0
    halfLayer = 0


# class de recuperation des données
class generateData:
    xDelta = 0
    yDelta = 0
    xStart = 0
    yStart = 0
    xEnd = 0
    yEnd = 0


# Calculer information
def getCalculInfo(gInfo):
    cData = generateData
    cData.xDelta = gInfo.X_box - gInfo.X_product
    cData.yDelta = gInfo.Y_box - gInfo.Y_product
    cData.xStart = (gInfo.X_product / 2)
    cData.yStart = (gInfo.Y_product / 2)
    cData.xEnd = gInfo.X_box - (gInfo.X_product / 2)
    cData.yEnd = gInfo.Y_box - (gInfo.Y_product / 2)
    return cData


# Recuperer informations
def getGeneralInfo():
    iPro = giveData
    iPro.X_product = int(SB_xProduct.get())
    iPro.Y_product = int(SB_yProduct.get())
    iPro.Z_product = int(SB_zProduct.get())

    iPro.X_box = int(SB_xBox.get())
    iPro.Y_box = int(SB_yBox.get())
    iPro.layerProduct_X = int(SB_xLayerProduct.get())
    iPro.layerProduct_Y = int(SB_yLayerProduct.get())
    iPro.nbrProduct = int(SB_nbrProduct.get())
    iPro.halfLayer = int(SB_halfLayer.get())
    return iPro


# Creation d'une couche
def setLayer(gInf, cInf):
    value = []
    tmp_dataCSV = []
    tmp_dataTXT = []
    deltaX = cInf.xDelta / (gInf.layerProduct_X - 1)
    deltaY = cInf.yDelta / (gInf.layerProduct_Y - 1)

    tmp_zLayer = 0
    n = 1
    for i in range(gInf.halfLayer):
        tmp_yLayer = int(cInf.yStart)
        for j in range(gInf.layerProduct_Y):
            tmp_xLayer = int(cInf.xStart)
            for k in range(gInf.layerProduct_X):
                row = []
                tmp_app = getApp(j,k,gInf)
                tmp_angle = getAngle(i)
                row.append(tmp_xLayer)
                row.append(tmp_yLayer)
                row.append(tmp_zLayer)
                row.append(tmp_angle)
                row.append(tmp_app)
                tmp_xLayer = tmp_xLayer + deltaX
                tmp_string = ("PERS patternpos pl_pat_pos" + str(n) + ":=[[" + str(tmp_xLayer) + "," + str(tmp_yLayer) + "," + str(tmp_zLayer) + "]," + str(tmp_angle) + "," + str(tmp_app) + "];")
                tmp_dataCSV.append(row)
                tmp_dataTXT.append(tmp_string)
                n += 1
            tmp_yLayer = int(tmp_yLayer + deltaY)
        tmp_zLayer = tmp_zLayer + gInf.Z_product
    value.append(tmp_dataTXT)
    value.append(tmp_dataCSV)
    return value


# definition de l'angle du produit
def getAngle(i):
    if (i%2==0):
        return 90
    else :
        return -90


# definition de l'approche robot à avoir
def getApp(j, k, g):
    if k == 0:
        if j == 0:
            x = 2
        elif j == (g.layerProduct_Y - 1):
            x = 4
        else:
            x = 7

    elif k == (g.layerProduct_X - 1):
        if j == 0:
            x = 8
        elif j == (g.layerProduct_Y - 1):
            x = 6
        else:
            x = 3
    else:
        if j == 0:
            x = 1
        elif j == (g.layerProduct_Y - 1):
            x = 5
        else:
            x = 0
    return x


# création d'un fichier CSV
def setCSV(r):
    name = I_name.get() + ".csv"
    with open(name, "w") as f_write :
        writer = csv.writer(f_write)
        writer.writerows(r)


# création d'un fichier TXT
def setTXT(r):
    name = I_name.get() + ".txt"
    file = open(name,'w')
    for item in r:
        print(item,file=file)
    file.close()


def main(event):
    generalInfo = getGeneralInfo()
    calculInfo = getCalculInfo(generalInfo)
    result = setLayer(generalInfo, calculInfo)
    setCSV(result[1])
    setTXT(result[0])


# Frame
F_choice = Frame(root, bg="white", borderwidth=2, relief=FLAT)
F_create = Frame(F_choice, borderwidth=2, relief=SUNKEN)
F_product = Frame(F_create, borderwidth=2, relief=SUNKEN)
F_box = Frame(F_create, borderwidth=2, relief=GROOVE)
F_layerProduct = Frame(F_create, borderwidth=2, relief=GROOVE)
F_nbrProduct = Frame(F_create, borderwidth=2, relief=GROOVE)
F_halfLayer = Frame(F_create, borderwidth=2, relief=GROOVE)

# Spinbox
SB_xProduct = Spinbox(F_product, from_=0, to=1000, value=10)
SB_yProduct = Spinbox(F_product, from_=0, to=1000, value=10)
SB_zProduct = Spinbox(F_product, from_=0, to=1000, value=2)
SB_xBox = Spinbox(F_box, from_=0, to=1000, value=100)
SB_yBox = Spinbox(F_box, from_=0, to=1000, value=50)
SB_xLayerProduct = Spinbox(F_layerProduct, from_=0, to=1000, value=10)
SB_yLayerProduct = Spinbox(F_layerProduct, from_=0, to=1000, value=5)
SB_nbrProduct = Spinbox(F_nbrProduct, from_=0, to=1000, value=500)
SB_halfLayer = Spinbox(F_halfLayer, from_=0, to=1000, value=3)

# Label
L_titre = Label(root, text="Gestion fichier csv")
L_product = Label(F_product, text="Produit : ")
L_box = Label(F_box, text="Carton : ")
L_layerProduct = Label(F_layerProduct, text="Nombre prod/cou : ")
L_nbrProduct = Label(F_nbrProduct, text="Nombre total de prduit : ")
L_halfLayer = Label(F_halfLayer, text="Nombre de sous-couche")

L_xProduct = Label(F_product, text="X:")
L_yProduct = Label(F_product, text="Y:")
L_zProduct = Label(F_product, text="Z:")
L_xBox = Label(F_box, text="X:")
L_yBox = Label(F_box, text="Y:")
L_xLayerProduct = Label(F_layerProduct, text="X:")
L_yLayerProduct = Label(F_layerProduct, text="Y:")

# Button
B_create = Button(F_create, text="generer")
B_close = Button(root, text="fermer", command=root.quit)

# Input
nameFile = StringVar()
nameFile.set("filename")
I_name = Entry(F_create, textvariable=nameFile, width=30)

# Generation Graphique
L_titre.pack()

F_product.pack()
L_product.pack()
L_xProduct.pack()
SB_xProduct.pack()
L_yProduct.pack()
SB_yProduct.pack()
L_zProduct.pack()
SB_zProduct.pack()

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
I_name.bind("<Return>", main)
I_name.pack()
F_create.pack(side=RIGHT, padx=30, pady=30)
B_create.bind("<Button-1>", main)
B_create.pack()

F_choice.pack()

B_close.pack()

# Fenetre
root.mainloop()
