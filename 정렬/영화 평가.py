import sys

N, L, H = map(int, sys.stdin.readline().strip().split())
scoreList = list(map(int, sys.stdin.readline().strip().split()))
scoreList.sort()
scoreList = scoreList[L:N-H]
print(sum(scoreList)/(N-L-H))