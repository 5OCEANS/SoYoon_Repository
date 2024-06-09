import sys

# A = 65
# a = 97

N = int(sys.stdin.readline().strip())
codeList = list(map(int, sys.stdin.readline().strip().split()))
stringList = list(sys.stdin.readline().strip())

for i in range(N):
  if codeList[i] == 0:
    codeList[i] = ' '
  elif codeList[i] >= 1 and codeList[i] <= 26:
    codeList[i] = chr(codeList[i] + 64)
  else:
    codeList[i] = chr(codeList[i] + 70)

if sorted(codeList) == sorted(stringList):
  print('y')
else:
  print('n')