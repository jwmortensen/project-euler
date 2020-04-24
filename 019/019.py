weekday = 1
monthday = 1
month = 1
year = 1900

long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]
while year < 1901:
    weekday = (weekday + 1) % 7
    monthday += 1
    if month in long_months and monthday > 31:
        month += 1
        monthday = 1
    elif month in short_months and monthday > 30:
    	month += 1
    	monthday = 1
    elif month == 2 and year % 4 != 0 and monthday > 28:
    	month += 1
    	monthday = 1
    
    
    	

