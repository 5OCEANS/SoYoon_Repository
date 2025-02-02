import sys
import math

def is_squarefree(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % (i * i) == 0:
      return False
  return True

n = int(sys.stdin.readline().strip())

for m in range(2, n):
  if is_squarefree(m * n):
    print(m)
    break