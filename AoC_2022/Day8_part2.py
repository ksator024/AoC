def checkSubstring(subString, max):
    count = 0
    for tree in subString:
        count += 1
        print(subString,max,tree)
        if tree >= max:
            return count
    return count

f = open("../Input.txt", "r")
trees = []

for line in f:
    trees.append([])
    for l in line:
        if l != "\n":
            trees[-1].append(int(l))

print(trees)
score = []
index = 0
for i in range(0,len(trees)):
    for j in range(0,len(trees[i])):
        count = 1
        index += 1
        tree = trees[i][j]
        y = []
        for k in range(0,len(trees)):
           y.append(trees[k][j])
        pos = []
        y1 = (y[:i])
        y1.reverse()
        y2 = y[i+1:]
        x1 = trees[i][j+1:]
        x2 = trees[i][:j]
        x2.reverse()
        pos.extend([x2,x1,y1,y2])
        for p in pos:
            #print("zahl", p)
            temp = checkSubstring(p,tree)
            count *= temp
            print(temp, index)
        print("new", count)
        score.append(count)

print(max(score))
print(score)