# 단순하게 푸는 답안 예시
N,M,K = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[N-1] # 가장 큰 수
second = data[N-2] # 두 번째로 큰 수

result = 0

while True:
  for i in range(K):
    if M == 0:
      break
    result += first
    M -= 1
  if M == 0:
    break
  result += second
  M -=1

print(result)

# 답안 예시
import sys

N, M, K = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort()
first = data[N-1]
second = data[N-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count * first)
result += ((M-count) * second)

print(result)