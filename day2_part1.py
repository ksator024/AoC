def isSave(li):
    mode = li[0] < li[1]  #false = desc
    for i in range(0,len(li)-1):
        if (li[i] > li[i+1] and mode is True) or (li[i] < li[i+1] and mode is False):
            return False
        distanz = li[i+1] - li[i]
        if  distanz not in range(-3,4) or distanz == 0:
            return False
    return True

f = open("C:\\Users\\mogri\\PycharmProjects\\AoC\\input.txt","r")
sum = 0
for line in f:
    li = line.split()
    intLi = []
    for l in li:
        l.strip()
        intLi.append(int(l))
    if(isSave(intLi)):
        sum +=1
print(sum)