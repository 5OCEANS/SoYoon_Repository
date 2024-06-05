import sys

string = sys.stdin.readline().strip()

prev = string[0]

zeroCnt = 0 
oneCnt = 0

for i in range(1, len(string)):
  if prev == string[i]:
    prev = string[i]
    continue
  else:
    if prev == '1':
      oneCnt += 1
    else:
      zeroCnt += 1
    prev = string[i]

print(max(zeroCnt, oneCnt))