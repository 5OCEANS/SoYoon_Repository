import sys

N = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())
numList = []
result = 0

for i in range(N-1):
  num = int(sys.stdin.readline())
  numList.append(num)

numList.sort(reverse=True)

if N == 1:
  print(0)
else:
  # 표가 제일 많은 후보를 찍으려고 하는 사람을 1명씩 매수
  while numList[0] >= dasom:
    result += 1
    dasom += 1
    numList[0] -= 1
    numList.sort(reverse=True)
  print(result)
