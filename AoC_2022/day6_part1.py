def checkSubline(Subline):
    for char in subLine:
        if subLine.count(char) > 1:
            return False
    return True



f = open("../Input.txt", "r")

line = f.readline()
index = 0
print(line)
for i in range(3,len(line)):
    subLine = line[i-3:i+1]
    print(subLine)
    if checkSubline(subLine):
        index = i +1
        break

print(index)