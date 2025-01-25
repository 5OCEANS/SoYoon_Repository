import sys

def count_intersections(T, test_cases):
  results = []
  for t in range(T):
    N, wires = test_cases[t]
    intersections = 0
    for i in range(N):
      for j in range(i + 1, N):
        A1, B1 = wires[i]
        A2, B2 = wires[j]
        if (A1 < A2 and B1 > B2) or (A1 > A2 and B1 < B2):
          intersections += 1
    results.append(f"Case #{t + 1}: {intersections}")
  return results

T = int(sys.stdin.readline())  
test_cases = []
for _ in range(T):
  N = int(sys.stdin.readline())  
  wires = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
  test_cases.append((N, wires))

results = count_intersections(T, test_cases)
print("\n".join(results))