import sys
n, k = map(int, input().split())

list = [int(sys.stdin.readline()) for __ in range(n)]

s = 1
e = max(list)

while s<= e:
  mid = (s + e) // 2 # 중간값
  lan = 0 # 잘라진 랜선 개수 초기화
  for i in list:
    lan += i // mid
  if lan >= k: # 필요한 랜선의 개수 이상을 만들 수 있는 경우
    s = mid + 1 
  else:
    e = mid - 1

print(e) # s > e 가 될 때, e 값이 가장 긴 랜선의 길이이다.