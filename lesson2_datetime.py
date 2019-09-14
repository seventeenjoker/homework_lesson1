from datetime import datetime, date, timedelta

'''
Задание
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/17 12:10:03.234567" в объект datetime
'''

dt_now = datetime.now()
print(f'Today is: {dt_now}')

delta_one_day = timedelta(days=1)
dt_yesterday = dt_now - delta_one_day
print(f'Yesterday was: {dt_yesterday}')

delta_one_month = timedelta(days=30)
dt_month_ago = dt_now - delta_one_month
print(f'One month ago was: {dt_month_ago}')

date_string = '01/01/17 12:10:03.234567'
date_time = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(f'String to time: {date_time}')