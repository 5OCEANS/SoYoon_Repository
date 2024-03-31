import sys

N = int(sys.stdin.readline())

nameList = []

for i in range(N):
  name = sys.stdin.readline().strip()

  nameList.append(name)

if 'anj' in nameList:
  print('뭐야;')
else:
  print('뭐야?')