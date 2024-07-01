# 시간 초과
# import sys

# S, P = map(int, sys.stdin.readline().strip().split())
# string = sys.stdin.readline().strip()
# A, C, G, T = map(int, sys.stdin.readline().strip().split())
# cnt = 0

# for i in range(S-P):
#   key = string[i:i+P]
#   if key.count('A') < A or key.count('C') < C or key.count('G') < G or key.count('T') < T:
#     continue
#   else:
#     cnt += 1

# print(cnt)

# 슬라이딩 윈도우 기법
import sys

S, P = map(int, sys.stdin.readline().strip().split())
string = sys.stdin.readline().strip()
A, C, G, T = map(int, sys.stdin.readline().strip().split())

cnt = 0

# 현재 윈도우 내 각 문자의 개수를 저장하는 딕셔너리
current_count = {
  'A': 0,
  'C': 0,
  'G': 0,
  'T': 0
}

# 첫 번째 윈도우 초기화
for i in range(P):
  current_count[string[i]] += 1

# 첫 번째 윈도우가 조건을 충족하는지 확인
if current_count['A'] >= A and current_count['C'] >= C and current_count['G'] >= G and current_count['T'] >= T:
  cnt += 1

# 윈도우를 이동하면서 조건을 확인
for i in range(P, S):
  # 새로운 문자를 윈도우에 추가
  current_count[string[i]] += 1
  # 윈도우에서 빠진 문자를 제거
  current_count[string[i - P]] -= 1
  
  # 현재 윈도우가 조건을 충족하는지 확인
  if current_count['A'] >= A and current_count['C'] >= C and current_count['G'] >= G and current_count['T'] >= T:
    cnt += 1

print(cnt)
