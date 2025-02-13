import fileinput
filepath = 'data/5.txt'
sum = 0
first = []
second = []
updates = []
incorrects = []
for line in fileinput.input(filepath, inplace = False):
    if line.__contains__("|"):
        l = line.rstrip().split("|")
        first.append(l[0])
        second.append(l[1])
    elif line.__contains__(","):
        l = line.rstrip().split(",")
        updates.append(l)

for u in updates:
    isOk = True
    for i in range(0,len(first)):
        if u.__contains__(first[i]) and u.__contains__(second[i]):
            if(u.index(first[i]) > u.index(second[i])):
                isOk = False
    if isOk:
        middleIndex = int((len(u) - 1)/2)
        sum += int(u[middleIndex])
    else:
        incorrects.append(u)
print(sum)

sum = 0
for u in incorrects:
    while(True):
        isOk = True
        for i in range(0,len(first)):
            if u.__contains__(first[i]) and u.__contains__(second[i]):
                if(u.index(first[i]) > u.index(second[i])):
                    u.insert(0, u.pop(u.index(first[i])))
                    isOk = False
        if isOk:
            break
    middleIndex = int((len(u) - 1)/2)
    sum += int(u[middleIndex])
print(sum)