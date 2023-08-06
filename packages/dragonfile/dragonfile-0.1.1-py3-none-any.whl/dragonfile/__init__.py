import csv

def readFile(dFile, dSep, nColumn):

    columns = []

    with open(dFile, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=dSep)
        next(reader)

        for i, row in enumerate(reader):
            columns.append(row[nColumn])

    dictD = {"coluna"+str(nColumn): columns}
    nColumn += 1

    return dictD, nColumn