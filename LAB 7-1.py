import datetime
now = datetime.datetime.now()
if now.hour < 12:
    ampm = '오전'
else:
    ampm = '오후'
hour_12 = now.hour % 12
if hour_12 == 0:
    hour_12 = 12
print("오늘의 날짜 : {}년 {}월 {}일".format(now.year, now.month, now.day))
print("현재시간 : {} {}시 {}분 {}초".format(ampm, hour_12, now.minute, now.second))
