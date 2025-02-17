import fileinput
filepath = 'data/6.txt'
steps = []
table = []
for line in fileinput.input(filepath, inplace = False):
    table.append(list(line.rstrip()))

for i in range(0, len(table)):
    try:
        position = [i,table[i].index("^")]
        break
    except ValueError:
        continue

dir = 0
while(True):
    if position[0] == 0 or position[1] == 0 or position[0] == len(table) -1 or position[1] == len(table[0])-1:
        break
    match dir:
        case 0:
            if table[position[0] -1][position[1]] == "#":
                dir = 1
            else:
                position[0] -= 1
                steps.append(str(position[0]) + str(position[1]))
                table[position[0]][position[1]] = "0"
        case 1:
            if table[position[0]][position[1] +1] == "#":
                dir = 2
            else:
                position[1] += 1
                steps.append(str(position[0]) + str(position[1]))
                table[position[0]][position[1]] = "0"
        case 2:
            if table[position[0] +1][position[1]] == "#":
                dir = 3
            else:
                position[0] += 1
                steps.append(str(position[0]) + str(position[1]))
                table[position[0]][position[1]] = "0"
        case 3:
            if table[position[0]][position[1] -1] == "#":
                dir = 0
            else:
                position[1] -= 1
                steps.append(str(position[0]) + str(position[1]))
                table[position[0]][position[1]] = "0"

steps = list(set(steps))
print(len(steps))

test = 0
for t in table:
    for i in t:
        if i == "0":
            test += 1
print(test)
