import calendar

# print(calendar.month(2023, 10, w=10, l=1))
# print(calendar.calendar(2023, w=0, l=0, c=0, m=6))

# print(calendar.weekday(2023, 10, 24))
# print(calendar.isleap(2023))
#
# print(calendar.leapdays(2000, 2020)) #v diapazone ne vkljucheno
# print(calendar.HTMLCalendar().formatyear(2023)) #create ne HTML file open in browser

import time
# print(time.time())

# start = time.time()
# # time.sleep(5) #vynuzdenaja pauza v sekundax
# stop = time.time()
# print(time.asctime()) #zapros lokalnogo vremeni iz brausera schityvaet
# print(time.gmtime())
# print(time.localtime()[0])
# print(stop - start)

import datetime

# d = datetime.date(1987, 11, 12)
# print(d)
# print(type(d))
# today = datetime.date.today()
# print(today)
# print(today - d)
# print(today.weekday())
# print(today.isoweekday())
# print(today.year)
# print(today.month)
# print(today.replace(2024))
#
# print(type(today - d))
# print(today - d)
#
# #date1 - date2 =timedelta
# #date1 -/+ timedelta = date2
# tdelta = datetime.timedelta(hours=10, minutes=15)

# next_birthday = datetime.date(2023, 11, 12)
# until_birthday = next_birthday - today
# print(until_birthday.total_seconds())

# t = datetime.time(13, 24, 43)
# print(t)
# print(type(t))
# now = datetime.time.

# dt = datetime.datetime(2023, 10, 24, 17, 23, 45)
# # print(dt)
# # print(type(dt))
# # print(dt.date())
# # print(dt.time())
# tdelta = datetime.timedelta(days=5, hours=12, minutes=37)
# print((dt - tdelta).time())
# today = datetime.datetime.now()
# print(today)
#
# ts = 574525800
# ts_date = datetime.date.fromtimestamp(ts)
# print(ts_date)
# ts_datetime = datetime.datetime.fromtimestamp(ts)
# print(ts_datetime)
#
# today_ts = today.timestamp()
# today_ts = datetime.datetime.timestamp(today)
# print(today_ts)

today = datetime.datetime.today()
today_str = today.strftime('%A, %d. %b %Y')

date_str = '24.10.23 20:20:15'
date_str = date_str.replace('Июнь', 'June')
d = datetime.datetime.strptime(date_str, '%d.%m.%y %H:%M:%S')
print(d)


