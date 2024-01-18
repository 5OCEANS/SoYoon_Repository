import sys

n = int(sys.stdin.readline())
pList = []
time = 0

pList = list(map(int, sys.stdin.readline().strip().split()))

pList.sort()

for i in range(1, n+1, 1):
  time += pList.pop()*i

print(time)