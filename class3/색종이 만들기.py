# 분할 정복: 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄여가는 방식

# 첫 색상이 나머지 색상과 같은지 확인 후 틀린 것이 있으면, 
# 틀린 구역을 다시 네 구역으로 나누어 다시 색상이 같은 것을 확인해주기 위해 재귀를 이용

# [x, y] [x, y + n/2]
# [x + n/2, y] [x + n/2, y + n/2]

import sys

n = int(sys.stdin.readline())

paper = []

for i in range(n):
  num = list(map(int, sys.stdin.readline().strip().split()))
  paper.append(num)

result = []

def solution(x, y, n):
  color = paper[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if color != paper[i][j]:
        solution(x, y, n//2)
        solution(x, y+n//2, n//2)
        solution(x+n//2, y, n//2)
        solution(x+n//2, y+n//2, n//2)
        return 
  if color == 0:
    result.append(0)
  else:
    result.append(1)

solution(0, 0, n)
print(result.count(0))
print(result.count(1))