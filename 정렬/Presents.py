import sys

N = int(sys.stdin.readline())
numdict = dict()
for _ in range(N):
  num = sys.stdin.readline().strip()
  numdict[float(num)] = num

sortedNumdictList = sorted(numdict.keys())
print(numdict[sortedNumdictList[1]])