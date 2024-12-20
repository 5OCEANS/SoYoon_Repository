import sys

def have_horizontal_straight_line(playerSpace):
  if (1, 1) in playerSpace and (1, 2) in playerSpace and (1, 3) in playerSpace:
    return True
  elif (2, 1) in playerSpace and (2, 2) in playerSpace and (2, 3) in playerSpace:
    return True
  elif (3, 1) in playerSpace and (3, 2) in playerSpace and (3, 3) in playerSpace:
    return True
  else:
    return False
  
def have_vertical_straight_line(playerSpace):
  if (1, 1) in playerSpace and (2, 1) in playerSpace and (3, 1) in playerSpace:
    return True
  elif (1, 2) in playerSpace and (2, 2) in playerSpace and (3, 2) in playerSpace:
    return True
  elif (1, 3) in playerSpace and (2, 3) in playerSpace and (3, 3) in playerSpace:
    return True
  else:
    return False
  
def have_diagonal(playerSpace):
  if (1, 1) in playerSpace and (2, 2) in playerSpace and (3, 3) in playerSpace:
    return True
  elif (1, 3) in playerSpace and (2, 2) in playerSpace and (3, 1) in playerSpace:
    return True
  else:
    return False

def is_win():
  global firstPlayerSpace
  global secondPlayerSpace
  if have_horizontal_straight_line(firstPlayerSpace) or have_vertical_straight_line(firstPlayerSpace) or have_diagonal(firstPlayerSpace):
    return 1
  elif have_horizontal_straight_line(secondPlayerSpace) or have_vertical_straight_line(secondPlayerSpace) or have_diagonal(secondPlayerSpace):
    return 2
  else:
    return 0

firstPlayerNumber = int(sys.stdin.readline())
secondPlayerNumber = 1 if (firstPlayerNumber == 2) else 2
firstPlayerSpace = []
secondPlayerSpace = []

for i in range(9):
  x, y = map(int, sys.stdin.readline().strip().split())
  if i % 2 == 0:
    firstPlayerSpace.append((x, y))
  else:
    secondPlayerSpace.append((x, y))
  num = is_win()
  if num == 0:
    continue
  elif num == 1:
    print(firstPlayerNumber)
    for i in range(i+1, 9):
      x, y = map(int, sys.stdin.readline().strip().split())
    break
  elif num == 2:
    print(secondPlayerNumber)
    for i in range(i+1, 9):
      x, y = map(int, sys.stdin.readline().strip().split())
    break
else:
  print(0)