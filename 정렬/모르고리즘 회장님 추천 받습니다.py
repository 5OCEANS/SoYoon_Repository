import sys

N = int(sys.stdin.readline())
pList = []

for i in range(N):
  p = list(sys.stdin.readline().strip().split())

  pList.append(p)

pList.sort(key=lambda x:(-int(x[1]), x[0]))

print(pList[0][0])