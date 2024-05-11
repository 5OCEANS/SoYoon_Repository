import sys

N = int(sys.stdin.readline())

seatList = sys.stdin.readline().strip()
cnt = 1
Lcnt= 0
for i in range(len(seatList)):
  if i == len(seatList)-1:
    cnt += 1
    break
  if seatList[i] == 'S':
    cnt += 1
    continue
  elif seatList[i] == 'L':
    Lcnt += 1
    if Lcnt == 1:
      continue
    elif Lcnt == 2:
      Lcnt = 0
      cnt += 1

if cnt >= len(seatList):
  cnt = len(seatList)

print(cnt)


n = int(input())
s = input()
if 'LL' in s:
  s = s.replace('LL', 's')
  print(len(s) + 1)
else:
  print(n)