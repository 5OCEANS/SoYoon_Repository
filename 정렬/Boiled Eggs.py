import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
  n, P, Q = map(int, sys.stdin.readline().strip().split())
  nList = list(map(int, sys.stdin.readline().strip().split()))
  nList.sort()
  sumWeight = 0
  count = 0
  for j in range(n):
    if sumWeight + nList[j] <= Q and count+1 <= P:
      count += 1
      sumWeight += nList[j]
    else:
      print('Case %d: %d' %(i+1, count))
      break
  else:
    print('Case %d: %d' %(i+1, count))