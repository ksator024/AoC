f = f = open("../Input.txt", "r")

fig = ["A","B","C","X","Y","Z"]

sum = 0
for line in f:

    l = line.split()
    numbers = []
    for char in l:
        numbers.append(fig.index(char) %3 )
    print(numbers)
    opp = numbers[0]
    you = numbers[1]
    sum += you +1
    if opp == (you - 1) % 3:
        print("sieg")
        sum += 6
    elif opp == you:
        print("un")
        sum += 3


    else:
        print("verloren")


print(sum)





