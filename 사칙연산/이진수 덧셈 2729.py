import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
  num1, num2 = sys.stdin.readline().strip().split()

  result = int(num1, 2) + int(num2, 2)

  print(bin(result)[2:])