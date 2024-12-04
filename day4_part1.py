def findCombinations(lines,lineCnt):
    line = lines[lineCnt]
    cnt = 0
    for i in range(0,len(line)): #loops horizontal
        hor = []
        ver = []
        dia = [[]] ##dia[0] -> unten rechts, dia[1] -> unten links
        dia.append([])
        for j in range(0,4):   ## extends 4 forwards
            if i<= len(line)-4:
                hor.append(line[i+j])
            if lineCnt + 4 <=len(lines):
                ver.append(lines[lineCnt+j][i])
            if i <= len(line)-4 and lineCnt + 4 <=len(lines):
                dia[0].append(lines[lineCnt+j][i+j])
            if lineCnt + 4 <=len(lines) and i >= 3:
                dia[1].append(lines[lineCnt+j][i-j])
        if containsXmas(hor):
            print(lineCnt," hor line:", i)
            cnt +=1
        if containsXmas(ver):
            print(lineCnt," ver line:", i)
            cnt +=1
        if containsXmas(dia[0]):
            print(lineCnt," dia rechts line:", i)
            cnt +=1
        if containsXmas(dia[1]):
            print(lineCnt,"dia link line:", i)
            cnt +=1
    return cnt

def containsXmas(list):

    s = ''.join(list)
    if not s.find("XMAS") == -1:
        return True
    s = ''.join(reversed(list))
    if not s.find("XMAS") == -1:
        return True
    return False


f = open("input.txt","r")
lines= []
sum = 0
for l in f:
    lines.append(l)
for i in range(0,len(lines)):
    sum += findCombinations(lines,i)

print(sum)