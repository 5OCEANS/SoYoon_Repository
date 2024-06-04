import sys

month, day, year, time = sys.stdin.readline().strip().split()

day = int(day[0:2])
year = int(year)

hour, minute = map(int, time.split(":"))

def convert_month_str_to_num(month_str):
  month_dict = {
    "January": 1, "February": 2, "March":3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
  }

  return month_dict[month_str]

month = convert_month_str_to_num(month)

# datetime 활용 - 아까 파싱한 값을 활용하여 datetime 객체를 만들고 datetime 객체끼리 계산하여 나온 timedelta 값을 활용
from datetime import datetime

total_year_datetime = datetime(year=year, month=12, day=31) - datetime(year=year-1, month=12, day=31)  # 그 해 총 시간
input_year_datetime = datetime(year=year, month=month, day=day, hour=hour, minute=minute) - datetime(year=year, month=1, day=1) # 지나간 시간

total_year_minute = total_year_datetime.days * 24 * 60 # 그 해 총 시간(단위: 분)
input_year_minute = input_year_datetime.days * 24 * 60 + input_year_datetime.seconds // 60 # 지나간 총 시간(초 단위도 포함함.)

print(input_year_minute / total_year_minute * 100)


# datetime 사용하지 않는 버전
def check_leap_year_or_not(year):
  is_leap_year = False

  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    is_leap_year = True

  return is_leap_year

def get_total_day_count(year, month=0, day=0):
  month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  total_day = sum(month_day_list)

  if month != 0 and day != 0:
    total_day = total_day - sum(month_day_list[month-1:]) + day - 1

  if check_leap_year_or_not(year=year) and (month > 2 or month == 0):
    total_day += 1
  
  return total_day

def get_total_minute_from_day(total_day, hour, minute):
  return total_day * 24 * 60 + hour * 60 + minute


total_year_day = get_total_day_count(year=year)
total_day = get_total_day_count(year=year, month=month, day=day)

total_year_minute = get_total_minute_from_day(total_day=total_year_day, hour=0, minute=0)

total_minute = get_total_minute_from_day(total_day=total_day, hour=hour, minute=minute)

print(total_minute/total_year_minute*100)