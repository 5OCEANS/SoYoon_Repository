import sys, math

N, W, H = map(int, sys.stdin.readline().strip().split())
limit = math.sqrt(W**2 + H**2)

for i in range(N):
  matches = int(sys.stdin.readline())
  if matches <= limit:
    print('DA')
  else:
    print('NE')