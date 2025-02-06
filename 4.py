import fileinput
filepath = 'data/4.txt'
sum = 0
temp = ""
#horzontal
table = []
#vertical
tableflip = []
#diagonals
tableside = []
tablesideflip = []

for line in fileinput.input(filepath, inplace = False):
    table.append(line.rstrip())

for i in range(0, len(table)):
    for j in range(0, len(table[0])):
        temp = temp + table[j][i]
    tableflip.append(temp)
    temp = ""

z = 0
while z < len(table) + len(table[0]):
    temp = ""
    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            if i + j == z:
                temp = temp + table[j][i]

    tableside.append(temp)
    z = z + 1

table.reverse()
z = 0
while z < len(table) + len(table[0]):
    temp = ""
    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            if i + j == z:
                temp = temp + table[j][i]

    tablesideflip.append(temp)
    z = z + 1

for i in table:
    sum += i.count("XMAS")
    sum += i.count("SAMX")
for i in tableflip:
    sum += i.count("XMAS")
    sum += i.count("SAMX")
for i in tableside:
    sum += i.count("XMAS")
    sum += i.count("SAMX")
for i in tablesideflip:
    sum += i.count("XMAS")
    sum += i.count("SAMX")

print(sum)