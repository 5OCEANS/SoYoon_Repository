import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  price = float(sys.stdin.readline().strip())

  print('$%0.2f' %(price * 0.8))