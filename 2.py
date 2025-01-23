import fileinput
filepath = 'data/2.txt'
sum = 0
ptwo = []
for line in fileinput.input(filepath, inplace = False):
    row = line.split()
    isOk = True
    first = True
    for i in range(0, len(row)):
        row[i] = int(row[i])
    
    if (row == sorted(row) or row == sorted(row, reverse=True)):
        for i in range(0, len(row) -1):
            if row[i] == row[i +1] or abs(row[i] - row[i +1]) > 3 or (row == sorted(row, reverse=True) and row[i] < row[i +1] or row == sorted(row) and row[i] > row[i +1]):
                isOk = False
                break
    else:
        isOk = False
    if isOk:
        sum += 1
    else:
        ptwo.append(row)
print(sum)

#part 2

for j in ptwo:
    for i in range(0, len(j)):
        temp = j.copy()
        temp.pop(i)
        isOk = True
        if (temp == sorted(temp) or temp == sorted(temp, reverse=True)):
            for x in range(0, len(temp) -1):
                if temp[x] == temp[x +1] or abs(temp[x] - temp[x +1]) > 3 or (temp == sorted(temp, reverse=True) and temp[x] < temp[x +1] or temp == sorted(temp) and temp[x] > temp[x +1]):
                    isOk = False
                    break
        else:
            isOk = False
        if isOk:
            sum += 1
            break
print(sum)