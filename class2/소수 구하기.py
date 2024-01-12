# 에라토스테네스의 체: 숫자의 제곱슨의 약수의 여부를 검증하면 된다.
n, m = map(int, input().split())

def isPrime(num):
  if num == 1:
    return False
  if num == 2:
    return True
  
  for i in range(2, int(num**0.5)+1):
    if num % i == 0:
      return False
  else:
    return True

for i in range(n, m+1):
  if isPrime(i):
    print(i)