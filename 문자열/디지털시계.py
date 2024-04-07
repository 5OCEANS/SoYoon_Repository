import datetime # 년, 월, 일, 시간, 분, 초, 마이크로초 등을 포함하는 datetime 객체를 생성 

from datetime import timedelta # 날짜와 시간을 연산할 수 있음. 두 날짜 또는 시간 간격을 나타냄.

for i in range(3):
  start, end = input().split()

  st = int(start.replace(":", ""))
  ed = int(end.replace(":", ""))

  stH, stM, stS = map(int, start.split(":"))
  edH, edM, edS = map(int, end.split(":"))

  stime = datetime.datetime(2024, 4, 7, stH, stM, stS)
  tmp_time = stime.strftime('%H%M%S') # datetime 객체를 지정한 포맷에 맞게 문자열로 변환하는 데 사용

  # 1씩 더하기 때문
  sec = 1

  cnt = 0
  if int(tmp_time) % 3 == 0:
    cnt += 1

  etime = datetime.datetime(2024, 4, 7, edH, edM, edS)
  etime = etime.strftime('%H%M%S')

  while True:
    if tmp_time == etime:
      break

    # sec만큼 증가 (여기서 sec는 1)
    stime = stime + timedelta(seconds = sec) 
    tmp_time = stime.strftime('%H%M%S')
    if int(tmp_time) %3 == 0:
      cnt += 1

  print(cnt)