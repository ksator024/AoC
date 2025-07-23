f = f = open("../Input.txt", "r")

fig = ["A","B","C","X","Y","Z"]

sum = 0
for line in f:

    l = line.split()
    numbers = []
    for char in l:
        numbers.append(fig.index(char) %3 )
    opp = numbers[0]
    goal = numbers[1]
    you = (opp + goal -1) % 3
    sum += you +1
    sum += goal*3
    print(goal*3)
    print(fig[you])

print(sum)








