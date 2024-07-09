import sys

N = int(sys.stdin.readline().strip())
cute = 0

for i in range(N):
  num = int(sys.stdin.readline())

  cute += num

if N // 2 >= cute:
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')