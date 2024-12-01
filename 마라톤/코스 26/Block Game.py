import sys

n = int(sys.stdin.readline().strip())
ans = [0] * 26

for _ in range(n):
  cnt = [[0] * 26 for _ in range(2)]
  words = sys.stdin.readline().strip().split()
  for i in range(2):
    for char in words[i]:
      cnt[i][ord(char) - ord('a')] += 1
  for i in range(26):
    ans[i] += max(cnt[0][i], cnt[1][i])

for count in ans:
  print(count)