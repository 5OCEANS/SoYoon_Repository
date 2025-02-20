import sys, bisect

def count_wins(A, B):
  B.sort()  # B를 정렬
  total = 0  # A가 B보다 큰 경우의 수를 저장

  for a in A:
    count = bisect.bisect_left(B, a)  # a보다 작은 B의 개수, 이진 탐색이 쉽게 구현될 수 있도록 하는 함수
    total += count

  return total

def better_dice(n, A, B):
  # 각각 A가 B보다 높은 경우의 수, B가 A보다 높은 경우의 수를 구함
  A_wins = count_wins(A, B)
  B_wins = count_wins(B, A)

  if A_wins > B_wins:
    return "first"
  elif A_wins < B_wins:
    return "second"
  else:
    return "tie"

# 입력 예제
n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

print(better_dice(n, A, B))