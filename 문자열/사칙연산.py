import sys

T = int(sys.stdin.readline())

for i in range(T):
  num1, operator, num2, equals, result = sys.stdin.readline().strip().split()

  num1 = int(num1)
  num2 = int(num2)
  result = int(result)

  actualResult = 0

  if operator == '+':
    actualResult = num1 + num2

  elif operator == '-':
    actualResult = num1 - num2
  elif operator == '*':
    actualResult = num1 * num2
  elif operator == '/':
    actualResult = num1 / num2

  if actualResult == result:
    print('correct')
  else:
    print('wrong answer')