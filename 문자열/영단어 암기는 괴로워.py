import sys

N , M = map(int, sys.stdin.readline().strip().split())
vocabDic = {}

for i in range(N):
  word = sys.stdin.readline().strip()
  if len(word) < M:
    continue

  vocabDic[word] = 1 if vocabDic.get(word) == None else 1 + vocabDic[word]

sorted_vocaDic = dict(sorted(vocabDic.items(), key= lambda x:(-x[1], -len(x[0]), x[0])))

for key, val in sorted_vocaDic.items():
  print(key)