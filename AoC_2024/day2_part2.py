def isSave(li):
    mode = li[0] < li[1]  #false = desc
    for i in range(0,len(li)-1):
        if (li[i] > li[i+1] and mode is True) or (li[i] < li[i+1] and mode is False):
            return False
        distanz = li[i+1] - li[i]
        if  distanz not in range(-3,4) or distanz == 0:
            return False
    return True

def checkLine(li):
    tempL = li.copy()
    if isSave(li):
        return True
    else:
        for i in range(0,len(li)):
            tempL.pop(i)
            if isSave(tempL):
                return True
            tempL = li.copy()
    return False
f = open("../Input.txt", "r")
sum = 0
for line in f:
    li = line.split()
    intLi = []
    for l in li:
        l.strip()
        intLi.append(int(l))
    if checkLine(intLi):
        sum +=1
print(sum)