import sys

X, C, K = map(int, sys.stdin.readline().strip().split())
applyList = []

for _ in range(K):
  T, S, N = map(int, sys.stdin.readline().strip().split())
  applyList.append((T, S, N))
applyList.sort()

seatDict = {}  # {학번: 좌석 번호}
seatOwner = {}  # {좌석 번호: 학번} (해당 좌석을 차지한 학생)

for _, S, N in applyList:
  # 신청한 좌석이 이미 다른 학생에 의해 점유된 경우 -> 신청 무효
  if S in seatOwner:
    continue  

  if N in seatDict:
    old_seat = seatDict[N]
    if old_seat in seatOwner:
      del seatOwner[old_seat]  # 기존 좌석 해제

  seatDict[N] = S
  seatOwner[S] = N  # 해당 좌석 점유 처리

for k in sorted(seatDict):
  print(k, seatDict[k])