import datetime

l=list()
for i in range(2):
    l.append(input().split(','))
dts = list()
for date in l:
    date[0] = date[0].split('/')
    date[1] = date[1].split(':')
    dts.append(datetime.datetime(int(date[0][2]), int(date[0][1]), int(date[0][0]), int(date[1][0]), int(date[1][1]), int(date[1][2])))

print(int(abs((dts[1]-dts[0]).total_seconds())))