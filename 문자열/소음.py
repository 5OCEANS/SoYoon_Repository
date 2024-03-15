import sys

A = int(sys.stdin.readline().strip())
operation = sys.stdin.readline().strip()
B= int(sys.stdin.readline().strip())

if operation == '*':
  print(A*B)
elif operation == '+':
  print(A+B)