import sys

N = int(sys.stdin.readline())

for i in range(N):
  string, num = sys.stdin.readline().strip().split('-')

  stringNum = 0

  for j in range(3):
    stringNum += (ord(string[j]) - 65) * pow(26, 2 - j)
  
  if abs(stringNum - int(num)) <= 100:
    print('nice')
  else:
    print('not nice')