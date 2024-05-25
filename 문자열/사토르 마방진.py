import sys

N = int(sys.stdin.readline())
stringList = []
rowStringList = ['' for _ in range(N)]

for i in range(N):
  string = sys.stdin.readline().strip()
  stringList.append(string)
  for j in range(N):
    rowStringList[j] += string[j]

for i in range(N):
  if stringList[i] != rowStringList[i]:
    print('NO')
    break
else:
  print('YES')

# zip 사용
import sys

n = int(sys.stdin.readline().rstrip())
w = [sys.stdin.readline().rstrip() for _ in range(n)]
zip_w = list(zip(*w)) # 병렬 처리 가능 

p = "YES"
for i in range(n):
  if w[i] != "".join(zip_w[i]):
    p = "NO"
    break
print(p)