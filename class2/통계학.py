# 시간초과
import sys
n = int(sys.stdin.readline())
numList = []
maxCntNum = -1
maxCnt = 0

for i in range(n):
  numList.append(int(sys.stdin.readline()))

print(round(sum(numList)/n))

numList.sort()
print(numList[round(n/2)])

numSetList = list(set(numList))
numSameCntList = []
for i in range(len(numSetList)):
  cnt = numList.count(numSetList[i])
  if maxCnt < cnt:
    maxCntNum = numSetList[i]
    maxCnt = cnt
  elif maxCnt == cnt:
    if maxCntNum not in numSameCntList:
      numSameCntList.append(maxCntNum)
    numSameCntList.append(numSetList[i])


if numSameCntList:
  numSameCntList.sort()
  print(numSameCntList[1])
else:
  print(maxCntNum)

minNum = min(numList)
maxNum = max(numList)

print(maxNum - minNum)

# 틀렸습니다
import sys
n = int(sys.stdin.readline())
numList = []
maxCnt = 0

for i in range(n):
  numList.append(int(sys.stdin.readline()))

print(round(sum(numList)/n))

numList.sort()
print(numList[round(n/2)])

# 최빈값
dic = dict()

for i in numList:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

mx = max(dic.values())
mx_dic = [] # 최빈값 숫자를 저장할 배열

for i in dic:
  if mx == dic[i]: # 최빈값의 key 저장
    mx_dic.append(i)
  
if len(mx_dic) > 1:
  print(mx_dic[1])
else:
  print(mx_dic[0])

minNum = min(numList)
maxNum = max(numList)

print(maxNum - minNum)

# 성공
import sys
input=sys.stdin.readline

n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])#2)

#최빈값
dic=dict()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
mx=max(dic.values())#빈도수 중 최대값 구하기
mx_dic=[]#최빈값 숫자를 저장할 배열

for i in dic:#빈도수 딕셔너리에서
    if mx==dic[i]:#최빈값의 key저장
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
    
print(max(arr)-min(arr))