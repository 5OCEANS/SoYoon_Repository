n = int(input())
cnt = 0

while n >= 0:
  # 5로 나누어진다면
  if n % 5 == 0:
    cnt += n // 5
    print(cnt)
    break
  # 5로 나누어지지 않을 경우 3킬로그램 봉지를 하나씩 추가해 줌
  n -= 3
  cnt += 1
else:
  print(-1)