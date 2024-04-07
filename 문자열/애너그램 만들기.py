import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

cnt = 0

for i in str1:
  if i not in str2:
    cnt += 1
  else:
    str2 = str2.replace(i, '', 1)

cnt += len(str2)

print(cnt)