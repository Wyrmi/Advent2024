import fileinput

filepath = 'data/8.txt'
table = []
nodes = {}
sum = 0
for line in fileinput.input(filepath, inplace = False):
    table.append(list(line.rstrip()))
#results = table[:]

def calcantis(a,b):
    dif = abs(a - b)
    if a < b:
        return (b + dif,a - dif)
    else:
        return (b - dif,a + dif)

def findantis(lis):
    temp = []
    for i in lis:
        temp = lis[lis.index(i) + 1:]
        for j in temp:
            x = calcantis(i[0],j[0])
            y = calcantis(i[1],j[1])
            
            if -1 < x[0] < len(table) and -1 < y[0] < len(table[0]):
                table[x[0]][y[0]] = "#"
            if -1 < x[1] < len(table) and -1 < y[1] < len(table[0]):
                table[x[1]][y[1]] = "#"

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
        