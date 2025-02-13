import sys

L = int(sys.stdin.readline())
rollcake = [0] * L
N = int(sys.stdin.readline().strip())
maxIndex = -1
expectedPiece = 0
actualMaxIndex = 0
actualMaxPiece = 0
for i in range(N):
  minNum, maxNum = map(int, sys.stdin.readline().strip().split())
  piece = maxNum - minNum + 1
  if expectedPiece < piece:
    maxIndex = i + 1
    expectedPiece = piece
  piece = 0
  for j in range(minNum-1, maxNum):
    if rollcake[j] == 0:
      rollcake[j] = i+1
      piece += 1
  if actualMaxPiece < piece:
    actualMaxIndex = i+1
    actualMaxPiece = piece

print(maxIndex)
print(actualMaxIndex)