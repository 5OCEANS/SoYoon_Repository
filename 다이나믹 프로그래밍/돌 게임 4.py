import sys

N = int(sys.stdin.readline())

def solution(n):
  dp = [0] * (n + 5)
  dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 1

  for i in range(5, n + 1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
      dp[i] = 0
    else:
      dp[i] = 1

  if dp[n] == 1:
    print('SK')
  else:
    print('CY')
  return dp[-1]

solution(N)


# 입력
n = int(input())

# DP
if n == 1:
  print('CY')
elif n == 2:
  print('SK')
elif n == 3:
  print('CY')
elif n == 4:
  print('SK')
else:
  dp = [-1] * (n+1)
  dp[1] = 'CY'
  dp[2] = 'SK'
  dp[3] = 'CY'
  dp[4] = 'SK'

  for i in range(5, n+1):
    # 돌을 1개 혹은 3개, 4개를 상근이가 선택하고 난 후 돌의 개수를 봤을 때 창영이가 이기는 상황이 한번이라도 있었다면 이번에는 상근이가 이기게 됨.
    # 왜냐하면 창근이가 이길 수 밖에 없는 상황이었지만, 상근이가 돌을 1개, 3개, 혹은 4개를 들고 오면서 그 상황을 자기 걸로 만들었기 때문이다.
    # 상근이가 시작해서 창영이가 이기는 패턴 -> 창영이가 시작해서 상근이가 이기는 패턴으로 만듦.
    if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
      dp[i] = 'SK'
    else:
      dp[i] = 'CY'
  print(dp[n])