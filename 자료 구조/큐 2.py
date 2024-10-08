# 시간 초과
import sys

N = int(sys.stdin.readline())
queue = []

for i in range(N):
  command = list(sys.stdin.readline().split())

  if command[0] == 'push':
    queue.append(int(command[1]))
  elif command[0] == 'pop':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue.pop(0))
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  elif command[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])

# 성공
import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline())

for _ in range(N) :
  i = sys.stdin.readline().split()

  if i[0] == 'push' :
    queue.append(int(i[1]))
  
  elif i[0] == 'pop' :
    if not queue :
      print (-1)
    else :
      print(queue[0])
      queue.popleft()
  
  elif i[0] == 'size' :
    print(len(queue))
  
  elif i[0] == 'empty' :
    if len(queue) == 0 :
      print(1)
    else :
      print(0)
  
  elif i[0] == 'front' :
    if not queue:
      print(-1)
    else :
      print(queue[0])
  
  elif i[0] == 'back' :
    if not queue :
      print(-1)
    else :
      print(queue[-1])