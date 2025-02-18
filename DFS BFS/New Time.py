import sys

firTimeH, firTimeM = map(int, sys.stdin.readline().strip().split(':'))
secTimeH, secTimeM = map(int, sys.stdin.readline().strip().split(':'))

firstTime = firTimeH*60 + firTimeM
secondTime = secTimeH*60 + secTimeM

ans = 0

if firstTime <= secondTime:
  interval = secondTime - firstTime
  ans += ((interval // 60) + (interval % 60))
else:
  interval = secondTime + (60*24 - firstTime)
  ans += ((interval // 60) + (interval % 60))
print(ans)