import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

cards.sort(reverse=True)

score = 0
while m > 0:
  if cards[0] > 0:
    score += cards[0]
    cards.pop(0)
    if len(cards) != 0:
      cards.pop()
  else:
    break
  if len(cards) == 0:
    break
  m -= 1

print(score)