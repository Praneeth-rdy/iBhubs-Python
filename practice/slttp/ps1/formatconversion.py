import datetime
def hours(h, f):
    h=int(h)
    if f=='AM':
        if h==12:
            return 0
        else:
            return h
    elif f=='PM':
        return h+12
    
month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

date = input().split(' ')

mon = month[date[0]]
year = int(date[2])
day = int(date[1])

date[3] = date[3].split(':')
hours = hours(date[3][0], date[3][1][2:])
minutes = int(date[3][1][:2])

print(datetime.datetime(year, mon, day, hours, minutes))