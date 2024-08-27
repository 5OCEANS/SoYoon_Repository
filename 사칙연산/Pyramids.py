import sys

while True:
  try:
    n = int(sys.stdin.readline())
    if n == 0:
      break
    total = 0
    for i in range(1, n+1):
      total += i
    print(total)
  except:
    break