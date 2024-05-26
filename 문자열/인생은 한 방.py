import sys

N = int(sys.stdin.readline())

S = sys.stdin.readline().strip()

length = 0

for i in range(len(S)-1):
  add = 1 if ord(S[i]) == ord(S[i+1]) - 1 or  ord(S[i]) == ord(S[i+1]) + 1 else 0

  length = length+1 if add == 1 else 0

  if length == 4:
    print('YES')
    break
else:
  print('NO')