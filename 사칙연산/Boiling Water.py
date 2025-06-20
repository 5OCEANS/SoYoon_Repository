import sys

B = int(sys.stdin.readline())
P = B*5-400
print(B*5-400)
if P < 100:
  print(1)
elif P == 100:
  print(0)
else:
  print(-1)