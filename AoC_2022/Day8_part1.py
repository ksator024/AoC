def checkSubstring(subString, max):

    for tree in subString:
        if tree >= max:
            return False
        #print("true",max, subString)
    return True

f = open("../Input.txt", "r")
trees = []

for line in f:
    trees.append([])
    for l in line:
        if l != "\n":
            trees[-1].append(int(l))

print(trees)
sum = 0
for i in range(0,len(trees)):
    for j in range(0,len(trees[i])):
        tree = trees[i][j]
        y = []
        for k in range(0,len(trees)):
           y.append(trees[k][j])
        pos = []
        y1 = y[:i]
        y2 = y[i+1:]
        x1 = trees[i][j+1:]
        x2 = trees[i][:j]
        pos.extend([x2,x1,y1,y2])
        for p in pos:
            #print("zahl", p)
            if checkSubstring(p, tree):
                print(tree)
                sum += 1
                break

print(sum)