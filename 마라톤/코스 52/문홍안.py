import sys

P = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
stoneList = [0] * 100
for i in range(N):
  loc, command = sys.stdin.readline().strip().split()
  if command == 'L':
    for j in range(0, int(loc)-1):
      stoneList[j] += 1
  elif command == 'R':
    for j in range(int(loc), 100):
      stoneList[j] += 1

blue = 0
red = 0
green = 0

for i in range(100):
  if stoneList[i] % 3 == 0:
    blue += 1
  elif stoneList[i] % 3 == 1:
    red += 1
  else:
    green += 1

print("%0.2f" % (P * (blue / 100.0)))
print("%0.2f" % (P * (red / 100.0)))
print("%0.2f" % (P * (green / 100.0)))