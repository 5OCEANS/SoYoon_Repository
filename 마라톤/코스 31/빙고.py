import sys

def is_bingo_width():
  global bingoList
  count = 0
  for i in range(5):
    if sum(bingoList[i]) == -5:
      count += 1
  return count

def is_bingo_length():
  global bingoList
  count = 0
  for i in range(5):
    if (bingoList[0][i]+bingoList[1][i]+bingoList[2][i]+bingoList[3][i]+bingoList[4][i]) == -5:
      count += 1
  return count

def is_bingo_diagonal():
  global bingoList
  count = 0
  if bingoList[0][0] + bingoList[1][1] + bingoList[2][2] + bingoList[3][3] + bingoList[4][4] == -5:
    count += 1
  if bingoList[0][4] + bingoList[1][3] + bingoList[2][2] + bingoList[3][1] + bingoList[4][0] == -5:
    count += 1
  return count

bingoList = list()
answerList = list()
count = 0

for i in range(5):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  bingoList.append(numList)

for i in range(5):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  answerList.append(numList)

for i in range(5):
  for j in range(5):
    for k in range(5):
      if answerList[i][j] in bingoList[k]:
        index = bingoList[k].index(answerList[i][j])
        bingoList[k][index]= -1
        count = (is_bingo_width() + is_bingo_length() + is_bingo_diagonal())
        if count >= 3:
          print(i*5+j+1)
          exit()