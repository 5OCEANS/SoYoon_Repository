import sys
from collections import deque

N = int(sys.stdin.readline())
washStack, dryStack = [], []

dish = 1
while True:
  c, d = map(int, sys.stdin.readline().strip().split())

  if c == 1:
    for i in range(d):
      washStack.append(dish)
      dish += 1
  else:
    if c == 2:
      for i in range(d):
        dryStack.append(washStack.pop(-1))
  
  if len(dryStack) == N:
    break

for i in range(N):
  print(dryStack.pop(-1))