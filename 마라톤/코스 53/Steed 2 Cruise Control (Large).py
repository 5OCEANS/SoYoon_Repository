import sys

def solve():
  D, N = map(int, sys.stdin.readline().strip().split())
  max_time_span = 0.0

  for _ in range(N):
    K, S = map(int, sys.stdin.readline().strip().split())
    time_span = (D - K) / S
    if time_span > max_time_span:
      max_time_span = time_span

  my_speed = D / max_time_span
  print("%0.6f"%(my_speed))

test_case = int(sys.stdin.readline().strip())
for i in range(test_case):
  print(f"Case #{i+1}: ", end='')
  solve()