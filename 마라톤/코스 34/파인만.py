import sys

# # 2개일 때
# 1 + 4 = 5
# # 3개일 때
# 1 + 4 + 9 = 13
# # 4개일 때
# 1 + 4 + 9 + 16
# # 5개일 때
# 1 + 4 + 9 + 16 + 25

while True:
  try:
    N = int(sys.stdin.readline().strip())
    if N == 0:
      break
    ans = 0
    for i in range(N+1):
      ans += i**2
    print(ans)
  except:
    break