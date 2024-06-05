import sys

N = int(sys.stdin.readline())
seatList = []

width = 0
height = 0

for i in range(N):
  seat = sys.stdin.readline().strip()
  seatList.append(seat)

  widthSeatList = seat.split('X')
  
  for j in range(len(widthSeatList)):
    if '..' in widthSeatList[j]:
      width += 1

seatList = list(zip(*seatList))

for i in range(N):
  heightSeatList = ''.join(seatList[i]).split('X')

  for j in range(len(heightSeatList)):
    if '..' in heightSeatList[j]:
      height += 1

print(width, height)