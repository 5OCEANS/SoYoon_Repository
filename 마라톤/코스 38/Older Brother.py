import sys, math

def is_prime_power(q):
  if q == 1:
    return "no"
  
  p = None
  for i in range(2, int(math.sqrt(q)) + 1):
    if q % i == 0:
      p = i
      break

  if p is None:
    return "yes"

  while q % p == 0:
    q //= p

  return "yes" if q == 1 else "no"

q = int(sys.stdin.readline())
print(is_prime_power(q))