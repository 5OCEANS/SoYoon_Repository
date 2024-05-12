import sys

message = sys.stdin.readline().strip()

x, y = 0, 0

for i in range(1, int(len(message)/2) + 1):
  for j in range(i, len(message)+1):
    if i*j == len(message):
      x, y = i, j
  
for i in range(x):
  for j in range(y):
    print(message[i+j*x], end = '')