import datetime as dt
today = dt.date.today()
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas- dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format( \
time_gap.days,time_gap.seconds // 3600))

import datetime as dt
today = dt.date.today()
new_year = dt.datetime(2036, 1, 1)
time_gap = new_year - dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
print('2036년 새해 까지는 {}일 {}시간 남았습니다.'.format( \
time_gap.days,time_gap.seconds // 3600))

import datetime as dt
today = dt.date.today()
birthday = dt.datetime(2027, 3, 14)
time_gap = birthday- dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
print('2027년 생일까지는 {}일 {}시간 남았습니다.'.format( \
time_gap.days,time_gap.seconds // 3600))
