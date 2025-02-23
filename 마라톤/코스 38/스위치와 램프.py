import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
lampList= [False] * M # 선택되면 True로 바뀜.
switchList = deque()
for i in range(N):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  switchList.append(numList[1:])

for i in range(N):
  for j in range(N-1):
    for lamp in switchList[j]:
      lampList[lamp-1] = True
  if sum(lampList) == M:
    print(1)
    exit()
  else:
    lampList = [False] * M
  popThing = switchList.popleft()
  switchList.append(popThing)
else:
  print(0)