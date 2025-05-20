import sys

set_nums = list(map(int, sys.stdin.readline().strip().split()))
set_nums.sort() 

ma = set_nums[6]
a = set_nums[0]
b = set_nums[1]
c = ma - a - b

print(a, b, c)