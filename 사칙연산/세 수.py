import sys

num1, num2, num3 = map(int, sys.stdin.readline().strip().split())

if num1 == num2 + num3:
  print('%d=%d+%d'%(num1, num2, num3))
elif num1 == num2 - num3:
  print('%d=%d-%d'%(num1, num2, num3))
elif num1 == num2 * num3:
  print('%d=%d*%d'%(num1, num2, num3))
elif num1 == num2 / num3:
  print('%d=%d/%d'%(num1, num2, num3))
elif num1 + num2 == num3:
  print('%d+%d=%d'%(num1, num2, num3))
elif num1 - num2 == num3:
  print('%d-%d=%d'%(num1, num2, num3))
elif num1 * num2 == num3:
  print('%d*%d=%d'%(num1, num2, num3))
elif num1 / num2 == num3:
  print('%d/%d=%d'%(num1, num2, num3))