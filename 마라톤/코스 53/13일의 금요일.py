import sys

n = int(sys.stdin.readline().strip())
cnt = 0
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yo = ["월", "화", "수", "목", "금", "토", "일"]
day = 13  

for i in range(2019, n + 1):
  if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
    m[1] = 29
  else:
    m[1] = 28

  for j in range(12):
    if yo[day % 7] == "금":
      cnt += 1
    day += m[j]

print(cnt)