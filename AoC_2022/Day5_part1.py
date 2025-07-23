
def move(count, origin, desti, crates):
    start = len(crates[origin])-count
    print("origin: " + str(crates[origin]))
    print("start " + str(start))
    subList = crates[origin][start:]
    print("sublist:" + str(subList))
    crates[origin] = crates[origin][:start]
    subList.reverse()
    crates[desti].extend(subList)
    print("Crates:" + str(crates))
    return crates


f = open("../Input.txt", "r")

lines = []


while True:
    line = f.readline()
    if line == "\n":
        break
    lines.append(line)

size = len(lines[-1].split())
lines.pop(-1)

crates= [[]]
for i in range(size-1):
    crates.append([])

for line in lines:
    index = 1
    count = 0
    while index <= len(line):
        if line[index] != " ":
            crates[count].insert(0,line[index])
        count += 1
        index += 4

for line in f:
    words = line.split()
    count = int(words[1])
    origin = int(words[3])-1
    desi = int(words[5])-1
    crates = move(count,origin,desi,crates)
result = ""

for crate in crates:
    result += crate[-1]

print(result)
