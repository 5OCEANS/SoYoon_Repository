import sys
from collections import deque

N = int(sys.stdin.readline())
numq = deque(enumerate(map(int, sys.stdin.readline().strip().split()))) # enumerate: deque에 인덱스와 값이 튜플로 묶여서 하나의 원소로 저장된다.
ans = []

while numq:
  idx, paper = numq.popleft()
  ans.append(idx + 1)

  if paper > 0:
    numq.rotate(-(paper - 1)) # rotate(-1)은 원형 큐를 반시계방향으로 1칸 회전시키고, rotate(1)은 시계방향으로 1칸 회전
  elif paper < 0:
    numq.rotate(-paper)

print(' '.join(map(str, ans)))