import sys

N = int(sys.stdin.readline())
condoList = []
candidate = 0

for i in range(N):
  D, C = map(int, sys.stdin.readline().strip().split())

  condoList.append([D, C])

condoList.sort()

cost = 10001

for i in condoList:
  temp = i[1]
  if temp < cost:
    cost = temp
    candidate += 1

print(candidate)