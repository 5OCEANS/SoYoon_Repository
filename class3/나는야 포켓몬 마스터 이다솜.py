# 시간 초과 
import sys
n, m = map(int, sys.stdin.readline().split())

dic = {}

for i in range(1, n+1):
  dic[i] = sys.stdin.readline()

for i in range(m):
  instruc = sys.stdin.readline()
  if instruc in '0123456789':
    print(dic[int(instruc)])
  else:
    convert_dic = {v:k for k,v in dic.items()}
    convert_dic.get(instruc)
    print(convert_dic.get(instruc))

# 성공 
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
  a = input().rstrip()  
  # sys 라이브러리를 사용할때는 한 줄 입력받고 rstrip()을 꼭 호출해야한다.
  # readline()은 \n도 받으므로, 이 공백문자를 제거하는 역할을 한다.
  dict[i] = a
  dict[a] = i

for i in range(m):
  quest = input().rstrip()
  if quest.isdigit():
    print(dict[int(quest)])
  else:
    print(dict[quest])