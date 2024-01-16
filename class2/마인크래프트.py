# 간단한 코드상에서는 Python3가 메모리, 속도 측에서 우세함.
# But 복잡한 코드(반복)을 사용하는 경우에서는 PyPy3가 우세함.
# 코드 상황에 맞추어 두 구현체를 적절하게 사용해야 한다.
import sys
n, m, b = map(int, sys.stdin.readline().split())

field = [list(map(int, sys.stdin.readline().split())) for __ in range(n)]
answer = sys.maxsize
idx = 0

for floor in range(257):  # 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.
  exceed_block, lack_block = 0, 0

  for i in range(n):
    for j in range(m):
      if field[i][j] > floor:
        exceed_block += field[i][j] - floor
      else:
        lack_block += floor - field[i][j]
  
  if exceed_block + b >= lack_block:  # 인벤토리에 블록이 충분히 들어있을 경우
    if (exceed_block * 2) + lack_block <= answer:  # 시간 측정
      answer = (exceed_block * 2) + lack_block
      idx = floor

print(answer, idx)