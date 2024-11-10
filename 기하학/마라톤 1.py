import sys

# n 이 3 이상이므로 모든 경우의 수를 구할 필요는 없다.
n = int(sys.stdin.readline())
data = []
for i in range(n):
  x, y = map(int, sys.stdin.readline().strip().split())
  data.append((x, y))

maxValue = 0

# ex) 1-2-3-4-5

for i in range(1, n-1):
  after_data = abs(data[i][0] - data[i + 1][0]) + abs(data[i][1] - data[i + 1][1]) # 2-3
  before_data = abs(data[i - 1][0] - data[i][0]) + abs(data[i - 1][1] - data[i][1]) # 1-2
  value = after_data + before_data - (abs(data[i - 1][0] - data[i + 1][0]) + abs(data[i - 1][1] - data[i + 1][1])) # (1-2-3) - (1-3)  기존의 거리와 체크포인트 한 개 건너뛴 거리 차이    뒤에 3-4-5는 어차피 빼기 계산으로 사라지기 때문에 이렇게 해도 됨.
  maxValue = max(value, maxValue)

totalValue = 0 # 총 거리

for i in range(1, n):
  totalValue = totalValue + abs(data[i - 1][0] - data[i][0]) + abs(data[i - 1][1] - data[i][1])

print(totalValue - maxValue) # (1-2-3-4-5) - ((1-2-3) - (1-3)) = (1-3-4-5)