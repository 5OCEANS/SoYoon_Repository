import sys

N, M = map(int, sys.stdin.readline().strip().split())

blockList = []

for i in range(N):
  block = sys.stdin.readline().strip()
  blockList.append(block)

bottomBlock = blockList[0]

for i in range(N-1):
  upBlock = blockList[i+1]

  for j in range(M):
    print(i, j, bottomBlock, upBlock, bottomBlock[M-j-1:M], upBlock[0:j+1])
    print(i, j, bottomBlock, upBlock, bottomBlock[0:j+1], upBlock[M-j-1:M])
    if bottomBlock[M-j-1:M] == upBlock[0:j+1]: # 아래에 있는 블록는 마지막 부분부터 시작하고, 위에 있는 블록은 처음 부분부터 시작.
      print(bottomBlock)
      bottomBlock = upBlock
      break
    elif bottomBlock[0:j+1] == upBlock[M-j-1:M]: # 아래에 있는 블록은 처음 부분부터 시작하고, 위에 있는 블록은 마지막 부분부터 시작.
      print(bottomBlock)
      bottomBlock = upBlock
      break
  else:
    print(0)
    break
else:
  print(1)



