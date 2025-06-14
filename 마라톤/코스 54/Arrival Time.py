import sys

def is_rush_hour(hour, minute):
  total_minutes = hour * 60 + minute
  morning_start = 7 * 60
  morning_end = 10 * 60
  evening_start = 15 * 60
  evening_end = 19 * 60
  return (morning_start <= total_minutes < morning_end) or (evening_start <= total_minutes < evening_end)

def compute_arrival_time(start_h, start_m):
  current_h = start_h
  current_m = start_m
  remaining = 120  

  while remaining > 0:
    if is_rush_hour(current_h, current_m):
      advance = 0.5
    else:
      advance = 1.0

    remaining -= advance
    current_m += 1
    if current_m == 60:
      current_m = 0
      current_h = (current_h + 1) % 24

  return f"{current_h:02d}:{current_m:02d}"


time_str = sys.stdin.readline().strip()
h, m = map(int, time_str.split(":"))
print(compute_arrival_time(h, m))