import fileinput
import re
filepath = 'data/3.txt'
sum = 0 
valids = []
for line in fileinput.input(filepath, inplace = False):
    #row = line.split()
    valids.extend(re.findall(r"mul\(\d+,\d+\)", line))

for i in valids:
    nums = list(map(int, re.findall(r'\d+', i)))
    sum += nums[0] * nums[1]

print(sum)
