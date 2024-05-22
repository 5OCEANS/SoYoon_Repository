import sys

N, I = map(int,sys.stdin.readline().split())

handleList = []

for i in range(N):
  string = sys.stdin.readline()

  handleList.append(string)

handleList.sort()

print(handleList[I-1])