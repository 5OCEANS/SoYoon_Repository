import sys

cnt = 1

while True:
  try:
    num1, operator, num2 = sys.stdin.readline().strip().split()

    num1 = int(num1)
    num2 = int(num2)

    result = False

    if operator == 'E':
      break

    elif operator == '>':
      result = (num1 > num2)
    elif operator == '>=':
      result = (num1 >= num2)
    elif operator == '<':
      result = (num1 < num2)
    elif operator == '<=':
      result = (num1 <= num2)
    elif operator == '==':
      result = (num1 == num2)
    elif operator == '!=':
      result = (num1 != num2)
    
    if result:
      print('Case %d: true' %(cnt))
    else:
      print('Case %d: false' %(cnt))

    cnt += 1
  
  except:
    break

