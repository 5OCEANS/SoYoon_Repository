import math

n1, n2 = map(int, input().split())

print(math.gcd(n1, n2))
print(math.lcm(n1, n2))

# math 라이브러리 사용 X
def gcd(n1, n2):
  for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
      return i

def lcm(n1, n2):
  for i in range(max(n1, n2), (n1*n2) +1):
    if i % n1 == 0 and i % n2 == 0:
      return i