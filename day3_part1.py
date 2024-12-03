def findString(line,start):
    begin=line.find("mul(",start)
    if begin == -1: # line is done, return -2
        return 0,-2
    comPos = line.find(",",begin,begin+8)
    bracketPos = line.find(")",comPos,comPos+5)
    if bracketPos == -1 or comPos == -1: # mul does not have , or )
        return 0,begin+1
    result = 0;
    num1 = line[begin+4:comPos]
    num2 = line[comPos+1:bracketPos]
    if  not num1.isdecimal() or not num2.isdecimal():
        return 0,begin+1
    result = int(num1)*int(num2)
    return result, bracketPos



f = open("C:\\Users\\mogri\\PycharmProjects\\AoC\\input.txt","r")
sum = 0
for line in f:
    temp = (0,0)
    while temp[1] != -2:
        temp = findString(line,temp[1])
        sum += temp[0]


print(sum)