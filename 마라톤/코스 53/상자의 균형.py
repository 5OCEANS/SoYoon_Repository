import sys

n, L = map(int, sys.stdin.readline().strip().split())

input_data = list(map(int, sys.stdin.readline().strip().split()))

sum_ = 0

for i in range(n-1, 0, -1):
  sum_ += input_data[i]
  m_senter = sum_ / (n-i)

  if m_senter <= input_data[i-1] - L or m_senter >= input_data[i-1] + L:
    print("unstable")
    exit()

print("stable")