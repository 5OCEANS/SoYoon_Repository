import sys

# 하루에서 열차가 지나가는 시간을 빼면 된다.

DAY = 86400 # 24시간 = 86,400초

c, h = map(int, sys.stdin.readline().strip().split())

timeline = [] # 상행선, 하행선 열차가 지나가는 시간

for i in range(c + h):
  h, m, s = map(int, sys.stdin.readline().strip().split(':'))
  timeline.append(h * 60 * 60 + m * 60 + s)
timeline.sort()

prev = -40
totalPassing = 0

for time in timeline:
  if time - prev >= 40:
    passing = 40
  else:
    passing = time - prev

  totalPassing += passing
  prev = time

print(DAY - totalPassing)
