import datetime

date = input().split(' ')
y = int(input())
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

year = int(date[2])
mon = month[date[0]]
day = int(date[1])

print(datetime.date(year, mon, day)+datetime.timedelta(days=y*365))