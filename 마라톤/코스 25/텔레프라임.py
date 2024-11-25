import sys, math

def is_prime_number(num):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      return False
  return True
  
num1, num2 = map(int, sys.stdin.readline().split())
newNum = int(str(num2)+str(num1))
if is_prime_number(num1) and is_prime_number(newNum):
  print('Yes')
else:
  print('No')