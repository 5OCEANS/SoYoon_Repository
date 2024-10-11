import sys
from collections import deque

N = int(sys.stdin.readline())

string = list(sys.stdin.readline())
skillStack = deque()
skillCount = 0

for i in string:
  if i.isdigit():
    skillCount += 1
  elif i == 'S' or i == 'L':
    skillStack.append(i)
  elif i == 'K':
    if 'S' in skillStack:
      skillStack.remove('S')
      skillCount += 1
    else:
      break
  elif i == 'R':
    if 'L' in skillStack:
      skillStack.remove('L')
      skillCount += 1

print(skillCount)