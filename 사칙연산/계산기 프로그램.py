import sys, math

result = int(sys.stdin.readline().strip())

while True:
  operator = sys.stdin.readline().strip()

  if operator == '=':
    print(result)
    break
  
  n2 = int(sys.stdin.readline().strip())

  if operator == '+':
    result += n2
  elif operator == '-':
    result -= n2
  elif operator == '*':
    result *= n2
  elif operator == '/':
    result = math.floor(result / n2)
