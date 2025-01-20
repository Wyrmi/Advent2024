import fileinput
filepath = 'data/2.txt'
sum = 0

for line in fileinput.input(filepath, inplace = False):
    row = line.split()
    isOk = True
    decends = True
    first = True
    for i in range(0, len(row)):
        row[i] = int(row[i])
    if (row[0] < row[1]):
        decends = False
    else:
        decends = True
    for i in range(0, len(row) -1):
        if row[i] == row[i +1] or abs(row[i] - row[i +1]) > 3 or (decends and row[i] < row[i +1] or not decends and row[i] > row[i +1]):
            isOk = False
    if isOk:
        sum += 1
print(sum)