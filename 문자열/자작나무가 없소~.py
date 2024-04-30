import sys

N, S = sys.stdin.readline().strip().split()

cnt = 0

for i in range(int(N)):
  string, itemCnt = sys.stdin.readline().strip().split()

  stringList = string.split('_')

  if S in stringList:
    cnt += int(itemCnt)

print(cnt)