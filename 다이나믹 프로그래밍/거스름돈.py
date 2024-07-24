import sys

# 5로 나누었을 때 나머지가 0이면 그냥 몫이 정답이 됨
# (5로 나누었을 때의 나머지)를 2로 나누었을 때의 나머지가 0이라면 그 몫을 그냥 더해줌.
# 만약 나머지가 1이라면 (그 몫 - 1)을 해준 다음 그 값을 2로 나눈 몫을 더해줌.

n = int(sys.stdin.readline())

if n % 5 == 0:
  print(n//5)
elif n == 3 or n == 1:
  print(-1)
elif (n%5) % 2 == 0:
  print(n//5 + (n%5)//2)
elif (n%5) % 2 == 1:
  print((n//5)-1 + ((n%5) + 5)//2)
else:
  print(-1)