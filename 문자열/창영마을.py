import sys

ball = [1, 0, 0]

string = list(sys.stdin.readline().strip())

for i in string:
  if i == "A":
    tmp = ball[0]
    ball[0] = ball[1]
    ball[1] = tmp
  elif i == "B":
    tmp = ball[1]
    ball[1] = ball[2]
    ball[2] = tmp
  elif i == "C":
    tmp = ball[0]
    ball[0] = ball[2]
    ball[2] = tmp

print(ball.index(1) + 1)