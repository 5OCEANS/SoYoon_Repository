import sys

weight = float(sys.stdin.readline())
height = float(sys.stdin.readline())
bmi = weight/(height*height)

if bmi > 25:
  print('Overweight')
elif 18.5 <= bmi <= 25.0:
  print('Normal weight')
else:
  print('Underweight')