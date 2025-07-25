
# Objekt Orientierter Ansatz. Sicher auch simpler Lösbar




class Ordner:
    def __init__(self, name):
        self.name = name
        self.ordnerLs = []
        self.dateiLs = []

    def __str__(self):
        return self.name

    def addDatei(self, datei):
        self.dateiLs.append(datei)

    def addOrdner(self, ordner):
        self.ordnerLs.append(ordner)

    def getOrdner(self, name):
        for ordner in self.ordnerLs:
            if ordner.name == name:
                return ordner
        neuer_ordner = Ordner(name)
        self.addOrdner(neuer_ordner)
        return neuer_ordner

    def size(self):
        summe = 0
        for datei in self.dateiLs:
            summe += datei.size
        for ordner in self.ordnerLs:
            summe += ordner.size()
        return summe
    def ausgabe(self, striche):
        print(striche + self.name + " (dir)")
        striche = "     " + striche
        for ordner in self.ordnerLs:
            ordner.ausgabe(striche)
        for datei in self.dateiLs:
            print(striche + datei.name + " (File)")
        return "fertig"
    def loopAll(self, needSpace):
        deleteLs = []
        for ordner in self.ordnerLs:

            tempSize = ordner.size()

            if tempSize > needSpace:
                deleteLs.append(tempSize)
            deleteLs.extend(ordner.loopAll(needSpace))
        return deleteLs


class Datei:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __str__(self):
        return self.name

# Testcode / Beispiel zum Einlesen:
f = open("../Input.txt", "r")

currentOrdner = Ordner("root")
start = currentOrdner
path = []
path.append(currentOrdner)
for line in f:
    if line[0] == "$":
        if line[2] == "c":
            ziel = line.split()[-1]
            if ziel == "..":
                path.pop(-1)
                currentOrdner = path[-1]
            else:
                currentOrdner = currentOrdner.getOrdner(ziel)
                path.append(currentOrdner)
    else:
        stmts = line.split()
        if stmts[0] == "dir":
            currentOrdner.getOrdner(stmts[1])
            print()
        else:
            currentOrdner.addDatei(Datei(stmts[1], int(stmts[0])))

needSpace = 30000000 - (70000000 - path[0].size())


print(path[0].ausgabe("- "))

deletedList = path[0].loopAll(needSpace)
print(deletedList)


print(min(deletedList))