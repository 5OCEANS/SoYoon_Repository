import sys

while True:
  try:
    result = 0
    numSet = set(list(map(int, sys.stdin.readline().strip().split())))
    if -1 in numSet:
      break
    numSet.remove(0)
    for i in numSet:
      if (i * 2) in numSet:
        result += 1
    print(result)  
  except:
    break