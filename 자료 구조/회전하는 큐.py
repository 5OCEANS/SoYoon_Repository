import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
index = list(map(int, sys.stdin.readline().strip().split()))
dq = deque([i for i in range(1, N+1)])

count = 0
for i in index:
  while True:
    if dq[0] == i:
      dq.popleft()
      break
    else:
      if dq.index(i) < len(dq) / 2:
        while dq[0] != i:
          dq.append(dq.popleft())
          count += 1
      else:
        while dq[0] != i:
          dq.appendleft(dq.pop())
          count += 1
      
print(count)