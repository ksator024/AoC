def checkSubstring(subString, max):

    for tree in subString:
        if tree < max:
            return False
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
for i in range[0,len(trees)]:
    for j in range(0,len(trees)-1):
        substring = trees[j]
         if checkSubstring(substring, i):
             substring = []
             for k in range(0,len(trees[j])):
                 substring.append(trees[k][ ])
            sum +=1
