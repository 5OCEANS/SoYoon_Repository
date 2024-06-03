import sys

N = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

maxCnt = 0
maxChr = ''

alphabetList = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alphabetList)):
  chrCnt = string.count(alphabetList[i])

  if chrCnt > maxCnt:
    maxChr = alphabetList[i]
    maxCnt = chrCnt

print(maxChr, maxCnt)