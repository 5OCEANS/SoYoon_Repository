import sys

N, K = map(int, sys.stdin.readline().strip().split())
nList = list(map(int, sys.stdin.readline().strip().split()))
count = 0

for j in range(N-1, 0, -1):
  maxNumIndex = nList.index(max(nList[:j+1]))
  if maxNumIndex != j:
    nList[maxNumIndex], nList[j] = nList[j], nList[maxNumIndex]
    count += 1
    if count == K:
      print(nList[maxNumIndex], nList[j])
      break
  if nList == sorted(nList):
    print(-1)
    break
else:
  print(-1)   