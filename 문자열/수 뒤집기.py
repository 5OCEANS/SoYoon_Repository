import sys

N = int(sys.stdin.readline())

for i in range(N):
  num = sys.stdin.readline()

  numSum = int(num) + int(num[::-1])

  if str(numSum) == str(numSum)[::-1]:
    print('YES')
  else:
    print('NO')