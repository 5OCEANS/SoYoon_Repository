import sys
from collections import deque

N = int(sys.stdin.readline())
dequelist = deque()

for i in range(N):
  command = sys.stdin.readline().strip()

  if command[0] == '1':
    dequelist.appendleft(command.split()[1])
  elif command[0] == '2':
    dequelist.append(command.split()[1])
  elif command[0] == '3':
    if len(dequelist) > 0:
      print(dequelist.popleft())
    else:
      print(-1)
  elif command[0] == '4':
    if len(dequelist) > 0:
      print(dequelist.pop())
    else:
      print(-1)
  elif command[0] == '5':
    print(len(dequelist))
  elif command[0] == '6':
    if len(dequelist) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == '7':
    if len(dequelist) > 0:
      print(dequelist[0])
    else:
      print(-1)
  elif command[0] == '8':
    if len(dequelist) > 0:
      print(dequelist[-1])
    else:
      print(-1)
