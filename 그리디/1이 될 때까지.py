# 단순하게 푸는 답안 예시
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
  # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
  while n % k != 0:
    n -= 1
    result += 1
  # K로 나누기
  n //= k
  result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
  n -= 1
  result += 1

print(result)



# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식을 사용한 답안 예시
n, k = map(int, input().split())
result = 0

while True:
  # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += (n-target)
  n = target

  # N이 K보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 뺴기
result += (n-1)

print(result)