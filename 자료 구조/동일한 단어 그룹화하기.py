N = int(input())
groups = []
for i in range(N):
  word = sorted(list(input()))
  if word not in groups:
    groups.append(word)
print(len(groups))