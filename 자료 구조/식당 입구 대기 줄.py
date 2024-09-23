import sys
from collections import deque

n = int(sys.stdin.readline().strip())
stack = deque()
max = 0
result = ''

for i in range(n):
  command = sys.stdin.readline().strip()
  if command[0] == '1':
    stack.append(int(command.split()[1]))
  elif command[0] == '2':
    stack.popleft()
  
  if len(stack) > max:
    result = str(len(stack)) + ' ' + str(stack[-1])
    max = len(stack)
  elif len(stack) == max:
    if int(result.split()[1]) > stack[-1]:
      result = str(len(stack)) + ' ' + str(stack[-1])

print(result)