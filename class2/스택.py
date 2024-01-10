# 시간 초과
iCnt = int(input())
stack = []

for __ in range(iCnt):
  instruc = input()
  if 'push' in instruc:
    stack.append(instruc[5:])
  elif 'pop' in instruc:
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif 'size' in instruc:
    print(len(stack))
  elif 'empty' in instruc:
    if stack:
      print(0)
    else:
      print(1)
  elif 'top' in instruc:
    if stack:
      print(stack[-1])
    else:
      print(-1)

# input 대신 sys.stdin.readline() 사용
import sys 

iCnt = int(sys.stdin.readline())
stack = []

for __ in range(iCnt):
  instruc = sys.stdin.readline().split()
  if instruc[0] == 'push':
    stack.append(instruc[1])
  elif instruc[0] == 'pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif instruc[0] == 'size':
    print(len(stack))
  elif instruc[0] == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  elif instruc[0] == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)
