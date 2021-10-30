""" Упражнение 5
Разработать метод date_in_future(integer), который вернет дату через integer дней.
Если integer не является целым числом, то метод должен вывести текущую дату.
Формат возвращаемой методом даты должен иметь следующий вид '01-01-2001
22:33:44’. """

from datetime import datetime, timedelta

def date_in_future(day_offset):

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if day_offset:
        future = datetime.now() + timedelta(days = day_offset)
        dt_string_f = future.strftime("%d/%m/%Y %H:%M:%S")
        print(f"After {day_offset} days: {dt_string_f}")
    else:
        print(f"Current Date: {dt_string}")

date_in_future([]) # => текущая дата
date_in_future(2) # => текущая дата + 2 дня