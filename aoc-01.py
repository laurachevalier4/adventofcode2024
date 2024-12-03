import bisect

f = open("inputs/day1.txt")
lines = f.readlines()

total_diff = 0
left_list = []
right_list = []

for line in lines:
    nums = line.strip().split()
    bisect.insort(left_list, nums[0])
    bisect.insort(right_list, nums[1])

for i, num in enumerate(left_list):
    total_diff += abs(int(num) - int(right_list[i]))

print(total_diff)