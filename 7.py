import fileinput
filepath = 'data/7.txt'
results = []
values = []
sum = 0
for line in fileinput.input(filepath, inplace = False):
        l = line.rstrip().split(":")
        results.append(int(l[0]))
        vals = (l[1].split(" "))
        vals.pop(0)
        values.append(list(map(int, vals)))

def addmultiply(i,lis):
    if i == 0:
        return [lis[0]]
    else:
        add = []
        mul = []
        prev = addmultiply(i-1,lis)
        for p in prev:
            add.append(lis[i] + p)
            mul.append(lis[i] * p)
        return list(set(add + mul))
    
def parttwo(i,lis):
    if i == 0:
        return [lis[0]]
    else:
        add = []
        mul = []
        joi = []
        prev = parttwo(i-1,lis)
        for p in prev:
            add.append(lis[i] + p)
            mul.append(lis[i] * p)
            joi.append(int(''.join(map(str, [p,lis[i]]))))
        return list(set(add + mul + joi))

for i in range(0, len(results)):
    if results[i] in addmultiply(len(values[i])-1,values[i]):
         sum += results[i]

print(sum)

sum =0
for i in range(0, len(results)):
    if results[i] in parttwo(len(values[i])-1,values[i]):
        sum += results[i]

print(sum)