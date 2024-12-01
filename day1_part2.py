f = open("input.txt")

l1 = []
l2 = []
for line in f:
        line = line.split()
        l1.append(line[0].strip())
        l2.append(line[1].strip())
l1.sort()
l2.sort()
sum = 0
for a in l1:
    count = 0
    for b in l2:
        if int(a) == int(b):
            count+=1

    sum += int(a) * count
print(sum)