import sys

N = int(sys.stdin.readline())
numList = [i for i in range(N, 0, -1)]

for i in range(N-1):
  print(numList.pop(), end= ' ')
  numList.insert(0, numList.pop())

print(numList[0])


N = int(input())
card_list = [i for i in range(1, N+1)]
discarded_card = []

while len(card_list) != 1:
  discarded_card.append(card_list.pop(0)) #버리기
  card_list.append(card_list.pop(0)) #뒤로 옮기기

for i in discarded_card:
  print(i, end = ' ')
print(card_list[0])