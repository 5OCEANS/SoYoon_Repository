import sys

window = [[0]*2001 for _ in range(2001)]

for i in range(3):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
  x1 += 1000
  y1 += 1000
  x2 += 1000
  y2 += 1000

  for j in range(y1, y2):
    for k in range(x1, x2):
      if i != 2:
        window[k][j] = 1
      else:
        window[k][j] = 0

result = 0 
for i in range(2001):
  result += sum(window[i])

print(result)