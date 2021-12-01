import sys

prev_sum = sys.maxsize
num_increases = 0
nums = [int(line) for line in sys.stdin]
for i in range(len(nums)-2):
    sum = nums[i] + nums[i+1] + nums[i+2]
    if sum > prev_sum:
        num_increases += 1
    prev_sum = sum
print(num_increases)