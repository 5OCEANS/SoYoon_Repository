import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
  x = int(sys.stdin.readline().strip())
  print('YES') if x%9==0 else print('NO')