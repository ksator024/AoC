def checkUpdate(update, rules):
    for i in range(0,len(update)):
        page = update[i]
        if not checkSublist(page,update[i+1:],update[:i],rules):
            return False
    return True



def checkSublist(key,vorList,backList, rules):
    if key in rules:
        for number in vorList:
            if not number in rules[key]:
                return False
        for number in backList:
            if number in rules[key]:
                return False
    return True


f = open("input.txt","r")
sum = 0
rules = {}
updates = []
mode = True
for l in f:
    if l == '\n':
        mode = False
        continue
    if mode:
        line = l.split("|")
        line[1] =line[1].strip('\n')
        if not int(line[0]) in rules:
            rules[int(line[0])] = []
        rules[int(line[0])].append(int(line[1]))
    else:
        line = l.split(",")
        temp = []
        for c in line:
            c.strip('\n')
            temp.append(int(c))
        updates.append(temp)
for u in updates:
    if checkUpdate(u,rules):
        middle = u[int(len(u)/2)]
        sum += middle


print(sum)


f.close()