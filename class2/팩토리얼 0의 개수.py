import math

n = int(input())

nFactorialString = str(math.factorial(n))
zeroCnt = 0

for i in range(len(nFactorialString)):
  if nFactorialString[len(nFactorialString)-1-i] == '0':
    zeroCnt += 1
  else:
    break

print(zeroCnt)



