import sys

N = int(sys.stdin.readline())

string = sys.stdin.readline().strip()
conversionString = string[11:-11]

if len(string) <= 25: # 규칙 1의 경우
  print(string)
else:
  if conversionString[1:-1].count('.') >= 1: # 규칙 3의 경우
    print(string[0:9] + '......' + string[-10:])
  else: # 규칙 2의 경우
    print(string[0:11] + '...' + string[-11:])
  