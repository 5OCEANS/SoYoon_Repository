import sys

N = int(sys.stdin.readline())
costList = [0 for _ in range(1002)]
standard = 0
for i in range(N):
  d, c = sys.stdin.readline().strip().split()
  if d == 'jinju':
    standard = int(c)
  else:
    costList[min(1001, int(c))] += 1
print(standard)
print(sum(costList[standard+1:]))