import sys

N = int(sys.stdin.readline())

if N == 23:
  print((45*15+15*60)*(N-2)+60*60*3)
elif 13 <= N < 23:
  print((45*15+15*60)*(N-1) + 60*60*2)
elif 3 <= N < 13:
  print((45*15+15*60)*N + 60*60*1)
else:
  print((45*15+15*60)*(N+1))

# 일반적인 시간 (1, 2, 4 ...) 일 때는 
# 초: 03, 13, 23, 43, 53, 30, 31 ~ 39 -> 15개
# 분: -> 15개

# 시: 3, 13, 23

# 분까지 총 몇 개: (45) * 15 + (15) * 60
# 시: 60 * 60


# 모범 답안
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)