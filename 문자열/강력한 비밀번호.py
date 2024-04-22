import sys

N = int(sys.stdin.readline())

S = sys.stdin.readline().strip()

numCnt = 0
lowerCnt = 0
upperCnt = 0
specialCnt = 0

specialChr = '!@#$%^&*()-+'

needCnt = 0

for i in S:
  if i.isdigit():
    numCnt += 1
  elif i.islower():
    lowerCnt += 1
  elif i.isupper():
    upperCnt += 1
  elif i in specialChr:
    specialCnt += 1

if numCnt <= 0:
  needCnt += 1
if lowerCnt <= 0:
  needCnt += 1
if upperCnt <= 0:
  needCnt += 1
if specialCnt <= 0:
  needCnt += 1
if N + needCnt < 6:
  needCnt = 6 - N

print(needCnt)