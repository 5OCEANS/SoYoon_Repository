import sys

for _ in range(4):
  dotList = list(map(int, sys.stdin.readline().strip().split()))
  firstLeftBottom = (dotList[0], dotList[1])
  firstRightTop = (dotList[2], dotList[3])
  secondLeftBottom = (dotList[4], dotList[5])
  secondRightTop = (dotList[6], dotList[7])

  if (firstLeftBottom[0] > secondRightTop[0]) or (firstRightTop[0] < secondLeftBottom[0]): # 첫 번째 사각형이 두 번째 사각형의 오른쪽에 있거나 왼쪽에 있어서 서로 공통 부분이 없을 때
    print('d')
    continue
  elif (firstLeftBottom[0] == secondRightTop[0]) or (firstRightTop[0] == secondLeftBottom[0]):
    if firstRightTop[1] < secondLeftBottom[1] or firstLeftBottom[1] > secondRightTop[1]:
      print('d')
      continue
    elif firstRightTop[1] == secondLeftBottom[1] or firstLeftBottom[1] == secondRightTop[1]:
      print('c')
      continue
    else:
      print('b')
      continue
  elif (firstLeftBottom[0] < secondRightTop[0]) and (firstRightTop[0] > secondLeftBottom[0]):
    if firstRightTop[1] < secondLeftBottom[1] or firstLeftBottom[1] > secondRightTop[1]:
      print('d')
      continue
    elif firstRightTop[1] == secondLeftBottom[1] or firstLeftBottom[1] == secondRightTop[1]:
      print('b')
      continue
    else:
      print('a')
      continue  