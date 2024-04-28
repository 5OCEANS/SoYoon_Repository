import sys

N = int(sys.stdin.readline())

card = {}
card = {'STRAWBERRY' : 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

for i in range(N):
  S, X = sys.stdin.readline().strip().split()
  card[S] += int(X)

for k, v in card.items():
  if v == 5:
    print('YES')
    break
else:
  print('NO')