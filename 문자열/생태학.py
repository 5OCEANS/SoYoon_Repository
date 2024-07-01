import sys

all = sys.stdin.readlines()
woodDic = {}
cnt = 0

for string in all:
  if string.strip() in woodDic:
    woodDic[string.strip()] += 1
  else:
    woodDic[string.strip()] = 1
  cnt += 1

sorted_woodDic = dict(sorted(woodDic.items(), key= lambda x:x[0]))

for key, val in sorted_woodDic.items():
  print('%s %.4f' %(key, (val/cnt)*100))