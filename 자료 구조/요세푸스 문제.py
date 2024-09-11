import sys

N, K = map(int, sys.stdin.readline().strip().split())

nList = [i+1 for i in range(N)]
index = 0

print('<', end = '')

for i in range(N-1):
  index += (K-1)
  if index >= len(nList):
    index -= len(nList)
    index %= len(nList)

  print(nList.pop(index), end = ', ')

print(str(nList[0]) + '>')

# 2 4 1 3 2 0 0 
# 6 5 4 3 2 1 0