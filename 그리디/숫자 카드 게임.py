import sys

N, M = map(int, sys.stdin.readline().strip().split())
maxNum = 0

for i in range(N):
  numList = list(map(int, sys.stdin.readline().strip().split()))
  minNum = min(numList)
  if maxNum <= minNum:
    maxNum = minNum
print(maxNum)

N, M = map(int)


# min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
  data=list(map(int, input().split()))
  # 현재 행에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(min_value, result)

print(result)


# 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data :
    min_value = min(min_value, a) # 행 내에서 가장 작은 숫자를 찾기
  # '가장 작은 수'들 중 가장 큰 수 찾기
  result = max(result, min_value)

print(result)