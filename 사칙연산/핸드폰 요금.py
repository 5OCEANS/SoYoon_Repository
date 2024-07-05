import sys

N = int(sys.stdin.readline().strip())

timeList = list(map(int, sys.stdin.readline().strip().split()))

youngsik = 0
minsik = 0

for i in range(N):
  youngsik += ((timeList[i] // 30 + 1) * 10)
  minsik += ((timeList[i] // 60 + 1) * 15)

if youngsik < minsik:
  print('Y', youngsik) 
elif youngsik == minsik:
  print('Y M', youngsik)
else:
  print('M', minsik)