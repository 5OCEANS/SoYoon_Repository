import sys

seatList = [['.' for _ in range(20)] for _ in range(10)]

N = int(sys.stdin.readline())

for i in range(N):
  seat = sys.stdin.readline().strip()

  row = ord(seat[0]) - 65
  number = int(seat[1:]) - 1

  seatList[row][number] = 'o'

for i in range(10):
  for j in range(20):
    print(seatList[i][j], end = '')
  print()