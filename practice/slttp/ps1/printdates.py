import datetime

date = input().split(' ')
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

year = int(date[2])
mon = month[date[0]]
day = int(date[1])

for i in [-1, 0, 1]:
    print(datetime.date(year, mon, day)+datetime.timedelta(days=i)) #you cannot directly keep day+i in datetime.date() because it doesn't work for day = 31