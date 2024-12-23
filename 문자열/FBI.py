import sys

ans = []

for i in range(5):
  name = sys.stdin.readline().strip()
  if 'FBI' in name:
    ans.append(str(i+1))

if ans == []:
  print('HE GOT AWAY!')
else:
  print(' '.join(ans))