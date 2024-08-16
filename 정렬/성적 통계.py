import sys

K = int(sys.stdin.readline())

for i in range(K):
  N, *nList = map(int, sys.stdin.readline().strip().split())
  print('Class ' + str(i+1))
  sortednList = sorted(nList, reverse=True)
  gap = 0
  for j in range(N-1, 0, -1):
    nowGap = sortednList[j-1] - sortednList[j]
    if gap < nowGap:
      gap = nowGap

  print('Max %d, Min %d, Largest gap %d' %(sortednList[0], sortednList[N-1], gap))
