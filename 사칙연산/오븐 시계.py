import sys

nowH, nowM = map(int, sys.stdin.readline().strip().split())

plusTime = int(sys.stdin.readline().strip())

plusM = plusTime % 60
plusH = plusTime // 60

if nowM + plusM > 59:
  plusH += (nowM + plusM) // 60
  nowM = (nowM + plusM) % 60
else:
  nowM = nowM + plusM

if nowH + plusH > 23:
  nowH = (nowH + plusH) % 24
else:
  nowH += plusH

print(nowH, nowM)