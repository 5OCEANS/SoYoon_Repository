import sys

s = sys.stdin.readline().strip()

total = set()

for i in range(len(s)):
  for j in range(i, len(s)):
    total.add(s[i:j+1]) # i번째 문자부터 부분 문자열 구하기

print(len(total))