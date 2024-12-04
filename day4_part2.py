

def containsMs(list):

    s = ''.join(list)
    if not s.find("MS") == -1:
        return True
    s = ''.join(reversed(list))
    if not s.find("MS") == -1:
        return True
    return False

def getCords(line, lineCount,lines):
    index = 1
    sum = 0

    while(line.find("A",index,len(line)-2) != -1):
        x = line.find("A",index,len(line)-2)
        index = x+1
        y = lineCount
        print(x,y)
        if correct(x,y,lines):
            sum +=1
    return sum
def correct(x,y,lines):
    pos1 = [(-1,-1),(1,1)]
    pos2 = [(1,-1),(-1,1)]
    l1 = []
    for pos in pos1:
        l1.append(lines[y+pos[1]][x+ pos[0]]) ## pos[1] = y, pos[0] = x
    if not containsMs(l1):
        return False
    l2 = []
    for pos in pos2:
        l2.append(lines[y+pos[1]][x + pos[0]]) ## pos[1] = y, pos[0] = x
    if not containsMs(l2):
        return False
    return True


f = open("input.txt","r")
lines= []
sum = 0
for l in f:
    lines.append(l)
for i in range(1,len(lines)-1):
    sum += getCords(lines[i], i, lines)

print(sum)