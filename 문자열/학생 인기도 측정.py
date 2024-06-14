import sys

n = int(sys.stdin.readline())
nameDic = {}

nameList = list(sys.stdin.readline().strip().split())

for i in range(len(nameList)):
  nameDic[nameList[i]] = 0

for i in range(n):
  stringList = sys.stdin.readline().strip().split()
  for j in range(len(stringList)):
    nameDic[stringList[j]] += 1

sorted_dict = dict(sorted(nameDic.items(), key=lambda x: x[1], reverse=True))

for key, val in sorted_dict.items():
  print(key, val)