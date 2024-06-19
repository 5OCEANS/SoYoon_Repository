# 틀렸습니다.
import sys

t = int(sys.stdin.readline())

for i in range(t):
  n = int(sys.stdin.readline())
  publicOneKey = sys.stdin.readline().strip().split()
  publicOneDic = {}
  for j in range(len(publicOneKey)):
    publicOneDic[publicOneKey[j]] = j

  publicTwoKey = sys.stdin.readline().strip().split()
  publicTwoList = []
  for j in range(len(publicTwoKey)):
    publicTwoList.append(publicOneDic[publicTwoKey[j]])

  secretString = sys.stdin.readline().strip().split()
  secretStringDic = {}
  for j in range(len(secretString)):
    secretStringDic[secretString[j]] = publicTwoList[j]
  
  sorted_secretStringDic = sorted(secretStringDic.items(), key= lambda x: x[1])

  for key, val in sorted_secretStringDic:
    print(key, end = ' ')
  print()


  # 0 1 2 3
  # 3 0 1 2

  # 3 0 1 2
  # C B A P
  # 0 1 2 3
  # B A P C

# 성공
import sys

t = int(input())
for i in range(t):
	plain = []
	n = int(input())
	pub_1 = list(sys.stdin.readline().split())
	pub_2 = list(sys.stdin.readline().split())
	cyper = list(sys.stdin.readline().split())
	d = {}
	for j in pub_2:
		d[pub_1.index(j)] = cyper.pop(0)
	sorted_d = " ".join(dict(sorted(d.items())).values())
	print(sorted_d)