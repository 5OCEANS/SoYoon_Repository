import sys

cu, du = map(int, sys.stdin.readline().strip().split())
cd, dd = map(int, sys.stdin.readline().strip().split())
cp, dp = map(int, sys.stdin.readline().strip().split())
h = int(sys.stdin.readline())
result = du + dd + dp

if result >= h:
  print(0)
  exit()

for i in range(min(cu,cd,cp), 5001):
  if i % cu == 0:
    result += du
  if i % cd == 0:
    result += dd
  if i % cp == 0:
    result += dp
  if result >= h:
    print(i)
    break