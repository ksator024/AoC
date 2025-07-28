def ausgabe(Hx,Hy,Tx,Ty):
    for i in range(7, -1,-1):
        ausgabe = ""
        for k in range(0, 7):
            if k == Hx and i == Hy:
                ausgabe += "H"
            elif k == Tx and i == Ty:
                ausgabe += "T"
            else:
                ausgabe += "."
        print(ausgabe)



def move(x,y,direction, distance):
    if direction == "U":
        y += distance
    elif direction == "D":
        y -= distance
    elif direction == "L":
        x -= distance
    elif direction == "R":
        x += distance
    return x,y

def getCorrection(Hx,Hy,Tx,Ty):
    xDiff = 0
    yDiff = 0
    if not Hx-Tx == 0:
        xDiff = (Hx-Tx)/abs(Hx-Tx)
    if not Hy - Ty == 0:
        yDiff = (Hy-Ty)/abs(Hy-Ty)

    return xDiff,yDiff


def checkTouching(Hx,Hy, Tx, Ty):
    if abs(Hx-Tx)<2 and abs(Hy-Ty)<2:
        return True
    return False








f = open("../Input.txt", "r")

Hx = 0
Hy = 0

Tx = 0
Ty = 0

path = []

ausgabe(Hx, Hy, Tx, Ty)

for line in f:
    direction = line.split()[0]
    distance = int(line.split()[1])
    for i in range(0,distance):
        temp = move(Hx,Hy,direction,1)
        Hx = temp[0]
        Hy = temp[1]
        print("")
        if not(checkTouching(Hx,Hy, Tx, Ty)):
            fix = getCorrection(Hx,Hy,Tx,Ty)
            print(fix)
            Tx += fix[0]
            Ty += fix[1]
            path.append((Tx,Ty))
        print(line)
        ausgabe(Hx,Hy,Tx,Ty)

print(len(set(path)))