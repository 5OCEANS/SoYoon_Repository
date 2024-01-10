from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque([])

for __ in range(n):
  instruc = sys.stdin.readline().split()

  if instruc[0] == 'push':
    queue.append(instruc[1])
  elif instruc[0] == 'pop':
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif instruc[0] == 'size':
    print(len(queue))
  elif instruc[0] == 'empty':
    if queue:
      print(0)
    else:
      print(1)
  elif instruc[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif instruc[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)