import sys

N = int(sys.stdin.readline())
count = 0
tlist = list()

for i in range(N):
  t = int(sys.stdin.readline())
  tlist.append(t)

time = 30
while True:
  if len(tlist) == 0:
    break
  if time == tlist[0]:
    count += 1
    tlist.pop(0)
  elif time > tlist[0]:
    time -= tlist[0]
    count += 1
    tlist.pop(0)
  else: # time < tlist[0]
    if time >= tlist[0] / 2: # 챕터를 절반 이상 공부할 수 있다면
      count += 1
    time = 30
    tlist.pop(0)

print(count)