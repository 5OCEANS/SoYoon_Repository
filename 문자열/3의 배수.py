import sys

num = list(sys.stdin.readline().strip())
cnt = 0

while len(num) > 1:
  sum = 0
  for i in range(len(num)):
    sum += int(num[i])

  num = list(str(sum))
  cnt += 1

print(cnt)
print('YES' if ''.join(num) == '3' or ''.join(num) == '6' or ''.join(num) == '9' else 'NO')