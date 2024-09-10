import sys

N = int(sys.stdin.readline())
numList = [i for i in range(N, 0, -1)]

for i in range(N-1):
  print(numList.pop(), end= ' ')
  numList.insert(0, numList.pop())

print(numList[0])