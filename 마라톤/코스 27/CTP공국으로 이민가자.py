import sys

T = int(sys.stdin.readline())
for _ in range(T):
  M, type = sys.stdin.readline().strip().split()
  if type == 'C': # 알파벳을 숫자로 바꾸는 문제
    stringList = list(sys.stdin.readline().strip().split())
    for i in range(int(M)):
      print(ord(stringList[i])-ord('A')+1, end=' ')
    print()
  elif type == 'N': # 숫자를 문자로 바꾸는 문제
    numList = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(int(M)):
      print(chr(numList[i]+ord('A')-1), end = ' ')
    print()