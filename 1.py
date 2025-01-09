import fileinput
filepath = 'data/1.txt'
sum = 0
left = []
right = []
for line in fileinput.input(filepath, inplace = False):
    nums = line.split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))
left.sort()
right.sort()
for i in range(0, len(left)):
    sum += abs(left[i] - right[i])
print(sum)