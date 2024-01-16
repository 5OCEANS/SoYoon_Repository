n, m = map(int, input().split())

dic = {}

for i in range(n):
  dic[i] = input()

for i in range(m):
  instruc = input()
  if instruc in '0123456789':
    print(dic[instruc])
  else:
    convert_dic = {v:k for k,v in dic.items()}
    convert_dic.get(instruc)