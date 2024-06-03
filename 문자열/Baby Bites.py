import sys

n = int(sys.stdin.readline())

numList = sys.stdin.readline().strip().split()

order = 1

for i in range(n):
  if numList[i].isdigit():
    if order == int(numList[i]):
      order += 1
      continue
    else:
      print('something is fishy')
      break
  else:
    order += 1
else:
  print('makes sense')