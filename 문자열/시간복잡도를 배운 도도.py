import sys

C = int(sys.stdin.readline())
maxLoop = 0

for i in range(C):
  string = sys.stdin.readline().strip()

  loopCnt = string.count('for')
  loopCnt += string.count('while')

  if maxLoop < loopCnt:
    maxLoop = loopCnt
    
print(maxLoop)