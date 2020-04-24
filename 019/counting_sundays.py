weekday = 1
monthday = 1
month = 1
year = 1900

long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]

n_sundays = 0
while year < 2001:
    is_century = year % 100 == 0
    is_leap_year = bool(year % 4 == 0 and not is_century) or year % 400 == 0
    if month in long_months and monthday > 31:
        month += 1
        monthday = 1
    elif month in short_months and monthday > 30:
    	month += 1
    	monthday = 1
    elif month == 2 and is_leap_year and monthday > 29:
        month += 1
        monthday = 1
    elif month == 2 and not is_leap_year and monthday > 28:
    	month += 1
    	monthday = 1
    if month > 12:
        year += 1
        month = 1
        monthday = 1
    if year > 1900 and year < 2001 and monthday == 1 and weekday == 0:
        n_sundays += 1
    weekday = (weekday + 1) % 7
    monthday += 1
print(n_sundays)
