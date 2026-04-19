import datetime as dt
print('오늘 =', dt.datetime.now())
thousand = dt.timedelta(days = 1000) 
plus1000day = dt.datetime.now() + thousand
print('1000일 후 =', plus1000day)

import datetime as dt
data = input("처음으로 사귄 연도와 월, 일을 입력하시오 : ")
y, m, d = map(int, data.split())
start_day = dt.datetime(y, m, d)
hundred_days = dt.timedelta(days=99)
anniversary = start_day + hundred_days
print("100일 기념일은 : {}년 {}월 {}일입니다.".format(anniversary.year, anniversary.month, anniversary.day))
