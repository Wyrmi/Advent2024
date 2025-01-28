import fileinput
import re
filepath = 'data/3.txt'
sum = 0 
valids = []
validstwo = []
doing = True
for line in fileinput.input(filepath, inplace = False):
    #row = line.split()
    valids.extend(re.findall(r"mul\(\d+,\d+\)", line))
    validstwo.extend(re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line))

for i in valids:
    nums = list(map(int, re.findall(r'\d+', i)))
    sum += nums[0] * nums[1]

print(sum)
sum = 0

for i in validstwo:
    if i == "do()":
        doing = True
    elif i == "don't()":
        doing = False
    if doing and i[0] == "m":
        nums = list(map(int, re.findall(r'\d+', i)))
        sum += nums[0] * nums[1]
print(sum)