import sys

N = int(sys.stdin.readline().strip())

# 만약 (n // 3)가 나머지가 없을 경우 창영이가 마지막 3개 묶음을 가져가게 된다.
# 나머지가 있다면 상근이가 마지막 3개 묶음을 가져가게 된다.

# 나머지가 2개 혹은 0개라면 시작한 사람이 마지막 돌을 가져가게 된다.
# 나머지가 1개라면 다른 사람이 마지막 돌을 가져가게 된다.

winner = 'who'

tmpNum = N % 3

if (N // 3) % 2 == 0:
  winner = 'CY'
else:
  winner = 'SK'

if tmpNum == 1:
  if winner == 'CY':
    winner = 'SK'
  else:
    winner = 'CY'

print(winner)