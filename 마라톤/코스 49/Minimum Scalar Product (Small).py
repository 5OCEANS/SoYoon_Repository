import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
  n = int(sys.stdin.readline().strip())
  v1List = list(map(int, sys.stdin.readline().strip().split()))
  v2List = list(map(int, sys.stdin.readline().strip().split()))
  v1List.sort(reverse=True)
  v2List.sort()
  sum = 0
  for j in range(n):
    sum += v1List[j] * v2List[j]
  print("Case #%d: %d" %(i+1, sum))