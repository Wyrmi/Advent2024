import fileinput

filepath = 'data/8.txt'
table = []
nodes = {}
sum = 0
for line in fileinput.input(filepath, inplace = False):
    table.append(list(line.rstrip()))
#results = table[:]

def findantis(lis):
    temp = []
    for i in lis:
        temp = lis[lis.index(i) + 1:]
        for j in temp:
            xdif = abs(i[0] - j[0])
            ydif = abs(i[1] - j[1])
            if i[0] < j[0]:
                x = j[0] + xdif
                xz = i[0] - xdif
            else:
                x = i[0] - xdif
                xz = j[0] + xdif
            if i[1] < j[1]:
                y = j[1] + ydif
                yz = i[1] - ydif
            else:
                y = j[1] - ydif
                yz = i[1] + ydif
            if -1 < x < len(table) and -1 < y < len(table[0]):
                table[x][y] = "#"
            if -1 < xz < len(table) and -1 < yz < len(table[0]):
                table[xz][yz] = "#"
            

for i in range(0, len(table)):
    for j in range(0, len(table[0])):
        if table[i][j] != '.':
            if table[i][j] in nodes:
                nodes[table[i][j]].append((i,j))
            else:
                nodes[table[i][j]] = [(i,j)]

for x in nodes:
    findantis(nodes[x])

for t in table:
    sum += t.count("#")
print(sum)

#for t in table:
#    print(''.join(map(str, t)))
        