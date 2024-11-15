# 신발끈 공식 사용. 완전 탐색

import sys

n = int(sys.stdin.readline())

def multiple(n, m): # 조합(combination) 계산에 이용
  s = 1
  for i in range(n, m-1, -1):
    s *= i
  return s

arr = []

for _ in range(n):
  arr.append(list(map(int, sys.stdin.readline().strip().split())))

i = 0 # 삼각형 인덱스1
j = 1 # 삼각형 인덱스2
k = 2 # 삼각형 인덱스3
m = 0 # 삼각형의 최대 넓이

for _ in range(multiple(n, n-3+1) // multiple(3, 1)): # 좌표 n 개에서 만들 수 있는 삼각형의 수는 n 개 중 3개를 뽑아 만들 수 있는 조합의 수 nC3 = (n*(n-1)*(n-2)) / (3*2*1)
  # 모든 조합 순회
  if k > n - 1: 
    j += 1 
    k = j + 1 
  if j > n - 2:
    i += 1
    j = i + 1
    k = j + 1

  pos1 = arr[i]
  pos2 = arr[j]
  pos3 = arr[k]

  area = abs(((pos1[0]*pos2[1]+pos2[0]*pos3[1]+pos3[0]*pos1[1]) - (pos1[1]*pos2[0]+pos2[1]*pos3[0]+pos3[1]*pos1[0]))/2)

  k += 1

  if m < area:
    m = area

print(m)