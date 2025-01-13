import sys

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()
string3 = sys.stdin.readline().strip()

ans = 0

if string1.isdigit() == True:
  ans = int(string1) + 3
elif string2.isdigit() == True:
  ans = int(string2) + 2
elif string3.isdigit() == True:
  ans = int(string3) + 1

if ans % 3 == 0 and ans % 5 == 0:
  print('FizzBuzz')
elif ans % 3 == 0:
  print('Fizz')
elif ans % 5 == 0:
  print('Buzz')
else:
  print(ans)