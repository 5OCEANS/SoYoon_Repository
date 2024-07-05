import sys

while True:
  N = sys.stdin.readline().strip()

  if N == '0':
    break

  res = len(N) + 1

  for i in N:
    if i == '1':
      res += 2
    elif i == '0':
      res += 4
    else:
      res += 3
  
  print(res)
