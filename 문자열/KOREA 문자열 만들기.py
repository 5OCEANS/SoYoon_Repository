import sys

S = sys.stdin.readline().strip()
korea = ['K', 'O', 'R', 'E', 'A']
cnt = 0

kNum = 0

for i in S:
  if i == korea[kNum]:
    kNum += 1
    cnt += 1
    if kNum > 4:
      kNum = 0

print(cnt)