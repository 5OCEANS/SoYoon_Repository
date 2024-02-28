import sys

ABCDList = list(map(int, sys.stdin.readline().strip().split()))

maxLevel = max(ABCDList)
minLevel = min(ABCDList)

ABCDList.remove(maxLevel)
ABCDList.remove(minLevel)

team1 = maxLevel + minLevel
team2 = sum(ABCDList)

print(abs(team1-team2))