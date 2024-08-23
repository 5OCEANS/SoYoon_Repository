import sys

numList = list(sys.stdin.readline().strip().split())

if int(numList[0]) + int(numList[2]) != int(numList[4]):
  print('NO')
else:
  print('YES')