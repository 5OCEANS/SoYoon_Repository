import sys
from collections import defaultdict

N = int(sys.stdin.readline())
groupDict = defaultdict(int)
for i in range(N):
  group = tuple(sorted(list(sys.stdin.readline().strip().split())))
  groupDict[group] += 1

print(max(groupDict.values()))