import datetime

date1 = input().split(' ')
date2 = input().split(' ')
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

year1 = int(date1[2])
mon1 = month[date1[0]]
day1 = int(date1[1])
year2 = int(date2[2])
mon2 = month[date2[0]]
day2 = int(date2[1])

date1 = datetime.date(year1, mon1, day1)
date2 = datetime.date(year2, mon2, day2)

for i in range((date2-date1).days + 1):
    print(date1+datetime.timedelta(days=i)) #you cannot directly keep day+i in datetime.date() because it doesn't work for day = 31