import sys

numList = sys.stdin.readline().strip().split()

B = sys.stdin.readline().strip()

cnt = 0

for i in numList:
  if i.startswith(B) and i != B:
    cnt += 1

print(cnt)