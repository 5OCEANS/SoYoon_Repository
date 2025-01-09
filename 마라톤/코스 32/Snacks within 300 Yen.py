import sys

while True:
  try:
    n = int(sys.stdin.readline().strip())
    if n == 0:
      break
    numList = list(map(int, sys.stdin.readline().strip().split()))
    total = 0
    for num in numList:  
      if total + num <= 300:
        total += num
    print(total)
  except:
    break