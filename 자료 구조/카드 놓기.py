# 재귀함수 사용
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = [sys.stdin.readline().strip() for _ in range(n)]
cards_list = []

def pick(result, n, picked):
  if n == k:
    if result not in cards_list:
      cards_list.append(result)
    return

  for card_idx in range(len(cards)):
    if card_idx not in picked:
      picked.append(card_idx)
      new_result = result + cards[card_idx]
      pick(new_result, n+1, picked)
      picked.pop()

pick("", 0, [])
print(len(cards_list))



# itertools 사용
import itertools
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = [sys.stdin.readline().strip() for _ in range(n)]
print(len(set("".join(i) for i in itertools.permutations(cards, k))))