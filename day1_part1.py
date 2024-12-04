f = open("input.txt","r")
l1 = []
l2 = []
for line in f:
        line = line.split()
        l1.append(line[0].strip())
        l2.append(line[1].strip())
l1.sort()
l2.sort()
sum = 0
for a in range(0,len(l1)):
    sum += abs(int(l1[a]) - int(l2[a]))
print(sum)