import sys

K = int(sys.stdin.readline().strip())

for data_set in range(1, K + 1):
    n, m = map(int, sys.stdin.readline().split())
    
    machines = []
    for _ in range(m):
        pi, ci, ui, ri = map(int, sys.stdin.readline().split())
        machines.append([pi, ci, ui, ri, 0])  # 마지막 요소는 실제 사용 횟수
    
    for _ in range(n):
        mj = int(sys.stdin.readline().strip()) - 1
        if machines[mj][4] < machines[mj][2]:  # 사용 가능 횟수 확인
            machines[mj][4] += 1
    
    profitable_machines = []
    for idx in range(m):
        pi, ci, ui, ri, used = machines[idx]
        revenue = used * ri
        cost = pi + (used * ci)
        if revenue > cost:
            profitable_machines.append(idx + 1)
    
    print(f"Data Set {data_set}:")
    for machine in sorted(profitable_machines):
        print(machine)
    print()
