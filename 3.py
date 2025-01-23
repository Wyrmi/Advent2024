import fileinput
import re
filepath = 'data/3.txt'
sum = 0 
valids = []
for line in fileinput.input(filepath, inplace = False):
    #row = line.split()
    valids = re.findall("mul\([0-9]+,[0-9]+\)+", line)

for i in valids:
    nums = list(map(int, re.findall(r'\d+', i)))
    sum += nums[0] * nums[1]
print(sum)
