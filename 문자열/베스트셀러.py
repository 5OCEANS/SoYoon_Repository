import sys

N = int(sys.stdin.readline().strip())
bookDic = {}

for i in range(N):
  string = sys.stdin.readline().strip()

  if string not in bookDic:
    bookDic[string] = 1
  else:
    bookDic[string] += 1

sorted_bookDic = dict(sorted(bookDic.items(), key=lambda x: (-x[1], x[0])))

for key, val in sorted_bookDic.items():
  print(key)
  break