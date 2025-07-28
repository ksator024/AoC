def ausgabe(Hx,Hy,knots):
    for i in range(10, -1,-1):
        ausgabe = ""
        for k in range(0, 10):
            temp = False
            if k == Hx and i == Hy:
                ausgabe += "H"
                temp = True
            for j in range(1,len(knots)):
                if knots[j][0] == k and knots[j][1] == i and not temp:
                    ausgabe += str(j)
                    temp = True
                    break
            if not temp:
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


knots = []
for i in range(0,9):
    knots.append((0,0))
Hx = knots[0][0]
Hy = knots[0][1]
path = []

ausgabe(Hx, Hy, knots)

for line in f:
    direction = line.split()[0]
    distance = int(line.split()[1])
    for i in range(0,distance):
        temp = move(knots[0][0D],knots[0][1],direction,1)
        knots[0] = (temp[0],temp[1])
        print("")
        for j in range(1, len(knots)):
            Tx = knots[j][0]
            Ty = knots[j][1]
            if not(checkTouching(knots[j-1][0],knots[j-1][1], Tx, Ty)):
                fix = getCorrection(knots[j-1][0],knots[j-1][1],Tx,Ty)
                print(fix)
                knots[j] = (knots[j][0] + fix[0],knots[j][1]+fix[0])
        ausgabe(knots[0][0], knots[0][1], knots)
        path.append(knots[-1])
        print(line)
print(len(set(path)))