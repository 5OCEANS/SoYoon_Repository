import sys

while True:
  try:
    num = int(sys.stdin.readline().strip())
    if num == 0:
      break
    cardList = list()
    for i in range(num):
      card = sys.stdin.readline().strip()
      cardList.append(card)
    for i in range(num//2):
      print(cardList[i])
      print(cardList[i+num//2+(num%2)])
    if num % 2 != 0:
      print(cardList[num//2])
  except:
    break