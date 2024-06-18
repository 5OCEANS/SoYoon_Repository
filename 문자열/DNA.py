import sys

#                       T A T G A T A C
#                       T A A G C T A C
#                       A A A G A T C C
#                       T G A G A T A C
#                       T A A G A T A C

# 가장 많이 나온 문자     T A A G A T A C   -> DNA

# 가장 많이 나온 문자를
#   제외한 문자 개수      1 1 1 0 1 0 2 1   -> Hamming Distance의 합 = 7

N, M = map(int, sys.stdin.readline().strip().split())
dnaList = []

for i in range(N):
  string = sys.stdin.readline().strip()
  dnaList.append(string)

rowDnaList = list(zip(*dnaList))

ansDNA = ''
hammingDistance = 0

for i in range(M):
  tCnt = ''.join(rowDnaList[i]).count('T')
  aCnt = ''.join(rowDnaList[i]).count('A')
  gCnt = ''.join(rowDnaList[i]).count('G')
  cCnt = ''.join(rowDnaList[i]).count('C')

  if aCnt == max(aCnt, cCnt, gCnt, tCnt):
    ansDNA += 'A'
    hammingDistance += (N - aCnt)
  elif cCnt == max(aCnt, cCnt, gCnt, tCnt):
    ansDNA += 'C'
    hammingDistance += (N - cCnt)
  elif gCnt == max(aCnt, cCnt, gCnt, tCnt):
    ansDNA += 'G'
    hammingDistance += (N - gCnt)
  else:
    ansDNA += 'T'
    hammingDistance += (N - tCnt)

print(ansDNA)
print(hammingDistance)