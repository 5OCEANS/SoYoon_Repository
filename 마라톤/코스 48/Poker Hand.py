import sys
from collections import defaultdict

handList = list(sys.stdin.readline().strip().split())
handDic = defaultdict(int)

for hand in handList:
  handDic[hand[0]] += 1
mostHand = sorted(handDic.items(), key=lambda x:-x[1])
print(mostHand[0][1])