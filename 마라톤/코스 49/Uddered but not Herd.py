import sys

cowphabet = sys.stdin.readline().strip()
bessie = sys.stdin.readline().strip()

cowphabet_len = len(cowphabet)
bessie_len = len(bessie)

pt = 0
pt2 = 0
ans = 1

while True:
  if pt2 == bessie_len:
    break
  if pt == cowphabet_len:
    pt = 0
    ans += 1
  if cowphabet[pt] == bessie[pt2]:
    pt2 += 1
    pt += 1
  else:
    pt += 1

print(ans)