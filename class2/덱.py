from collections import deque
import sys

iCnt = int(sys.stdin.readline())
deque = deque([])

for __ in range(iCnt):
  instruc = sys.stdin.readline().split()

  if instruc[0] == 'push_front':
    deque.appendleft(instruc[1])
  elif instruc[0] == 'push_back':
    deque.append(instruc[1])
  elif instruc[0] == 'pop_front':
    if deque:
      print(deque.popleft())
    else:
      print(-1)
  elif instruc[0] == 'pop_back':
    if deque:
      print(deque.pop())
    else:
      print(-1)
  elif instruc[0] == 'size':
    print(len(deque))
  elif instruc[0] == 'empty':
    if deque:
      print(0)
    else:
      print(1)
  elif instruc[0] == 'front':
    if deque:
      print(deque[0])
    else:
      print(-1)
  elif instruc[0] == 'back':
    if deque:
      print(deque[-1])
    else:
      print(-1)