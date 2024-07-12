import sys

num1, num2 = sys.stdin.readline().strip().split()

sum = int(num1, 2) + int(num2, 2)

print(bin(sum)[2:])