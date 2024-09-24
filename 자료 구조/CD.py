import sys

while True:
  try:
    N, M = map(int, sys.stdin.readline().strip().split())
    if N == 0 and M == 0:
      break
    cdSet = set()

    for i in range(N+M):
      num = int(sys.stdin.readline().strip())
      cdSet.add(num)
    
    print((N+M) - len(cdSet))

  except:
    break