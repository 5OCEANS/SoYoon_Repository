import sys

n = int(sys.stdin.readline())
sumresult = 0
for i in range(1, n-1):
  sumresult += ((i * (2 + (i-1)))//2)
print(sumresult)
print(3)