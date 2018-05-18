import csv

def openFile(filepath):
    with open(filepath, newline='') as csvfile:
        spamReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = []
        for row in spamReader:
            tmp = []
            for col in row:
                tmp.append(col)
            data.append(tmp)
    return data

def CheckDataPlace(data):
    for i, row in enumerate(data):
        if i >1:
            for j, col in enumerate(row):
                if (col==''):
                    print("ERREUR colonne = ",i,"ligne =",j)
                    return 1
    print("FILE OK!")
    return 0

def checkFile(filepath, event):
    data = openFile(filepath)
    CheckDataPlace(data)
