from datetime import datetime
input1 = 'Jan 1 2014 2:43PM'
date_format1 = '%b %d %Y %I:%M%p'
output1 = datetime.strptime(input1, date_format1)
print(f"Пример 1: {output1}")

input2 = '14:20 10/12/22'
date_format2 = '%H:%M %d/%m/%y'
output2 = datetime.strptime(input2, date_format2)
print(f"Пример 2: {output2}")

input3 = 'Tuesday, September 24, 2019'
date_format3 = '%A, %B %d, %Y'
output3 = datetime.strptime(input3, date_format3)
print(f"Пример 3: {output3}")

input4 = '01.01.1970 - 00:00:01'
date_format4 = '%d.%m.%Y - %H:%M:%S'
output4 = datetime.strptime(input4, date_format4)
print(f"Пример 4: {output4}")

from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(f"Вчера: {yesterday.strftime('%Y-%m-%d')}")
print(f"Сегодня: {today.strftime('%Y-%m-%d')}")
print(f"Завтра: {tomorrow.strftime('%Y-%m-%d')}")

from datetime import datetime

some_day = 1014163200
date_obj = datetime.fromtimestamp(some_day)
formatted_date = date_obj.strftime('%d.%m.%Y')
print(f"Преобразование временной метки {some_day} в {formatted_date} успешно!" )
