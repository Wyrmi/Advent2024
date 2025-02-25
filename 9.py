import fileinput
filepath = 'data/9.txt'
sum = 0
disk= []
isFile = True
for line in fileinput.input(filepath, inplace = False):
    for l in line:
        if isFile:
            for i in range(0,int(l)):
                disk.append(str(sum))
            sum += 1
        else:
            for i in range(0,int(l)):
                disk.append(".")
        isFile = not isFile

j = len(disk) -1
for i in range(0,len(disk)):
    if i >= j:
        break
    if disk[i] != ".":
        continue
    while disk[j] == ".":
        j -= 1
    disk[i] = disk[j]
    disk[j] = "."

sum = 0
for i in range(0,disk.index(".")):
    sum += i * int(disk[i])
print(sum)
