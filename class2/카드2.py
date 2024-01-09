# 시간 초과
numCnt = int(input())

numList = [num+1 for num in range(numCnt)]

while len(numList) > 1:
  numList.pop(0)
  popNum = numList.pop(0)
  numList.append(popNum)

print(numList[0])

# 성공 deque를 활용
from collections import deque
numCnt = int(input())
numDeque = deque([num+1 for num in range(numCnt)])

while len(numDeque)>1:
  numDeque.popleft()
  move_num = numDeque.popleft()
  numDeque.append(move_num)

print(numDeque[0])