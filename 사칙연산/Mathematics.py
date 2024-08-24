import sys

n = int(sys.stdin.readline())
sum = 0

for i in range(n):
  score = int(sys.stdin.readline())
  sum += score

print(sum)