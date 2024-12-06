import sys

N, M = map(int, sys.stdin.readline().strip().split())
stringList = list()
for i in range(N):
  string = sys.stdin.readline().strip()
  stringList.append(string[::-1])

for i in range(N):
  print(stringList[i])