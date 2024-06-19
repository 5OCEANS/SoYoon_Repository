import sys

S = sys.stdin.readline().strip()
SList = []

for i in range(len(S)):
  SList.append(S[i:])

SList.sort()

for i in range(len(SList)):
  print(SList[i])