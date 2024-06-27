import sys

N = int(sys.stdin.readline().strip())
extensionDic = {}

for i in range(N):
  extension = list(sys.stdin.readline().strip().split('.'))[1]
  
  extensionDic[extension] = 1 if extensionDic.get(extension) == None else 1 + extensionDic[extension]
  
sorted_extensionDic = dict(sorted(extensionDic.items(), key= lambda x: x[0]))

for key, val in sorted_extensionDic.items():
  print(key, val)



