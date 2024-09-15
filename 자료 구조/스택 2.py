import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for i in range(N):
  command = sys.stdin.readline().strip()

  if command[0] == '1':
    stack.append(command.split()[1])
  elif command == '2':
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  elif command == '3':
    print(len(stack))
  elif command == '4':
    if len(stack) > 0:
      print(0)
    else:
      print(1)
  elif command == '5':
    if len(stack) > 0:
      print(stack[-1])
    else:
      print( -1)