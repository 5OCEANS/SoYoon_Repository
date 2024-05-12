import sys

nopCnt = 0

string = sys.stdin.readline().strip()

for i in range(len(string)):
  if ord(string[i]) >= 65 and ord(string[i]) <= 90:
    if (i+nopCnt) % 4 == 0:
      continue
    else:
      nopCnt += (4 - ((i+nopCnt) % 4))

print(nopCnt)