import sys
from collections import deque

def rotate_word(w1, w2):
  if len(w1) != len(w2):
    return w2
  w2 = deque(w2)

  for _ in range(len(w2)):
    w2.rotate(1)
    t = ''.join(w2)
    if w1 == t:
      return t
  return ''.join(w2)

n = int(sys.stdin.readline())
stringList = [sys.stdin.readline().strip() for _ in range(n)]

for i in range(n):
  for j in range(i, n):
    if stringList[i]!= stringList[j]:
      stringList[j] = rotate_word(stringList[i], stringList[j])

print(len(set(stringList)))