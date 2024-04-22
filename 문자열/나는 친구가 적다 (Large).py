import sys

S = sys.stdin.readline().strip()

nums = '1234567890'

K = sys.stdin.readline().strip()

for i in nums:
  S = S.replace(i, '')

if K in S:
  print(1)
else:
  print(0)