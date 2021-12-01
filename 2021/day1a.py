import sys
 
# cat day1input.txt | python3 day1a.py
# answer: 1502

prev_num = sys.maxsize
num_increases = 0
for line in sys.stdin:
    curr_num = int(line)
    if curr_num > prev_num:
        num_increases += 1
    prev_num = curr_num
print(num_increases)
    