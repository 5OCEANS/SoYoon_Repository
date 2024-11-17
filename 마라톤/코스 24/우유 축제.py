import sys

N = int(sys.stdin.readline())
storeList = list(map(int, sys.stdin.readline().strip().split()))
order = 0
result = 0

for i in range(N):
  if storeList[i] == order % 3:
    result += 1
    order += 1

print(result)