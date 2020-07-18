import datetime

delta = datetime.timedelta(seconds = int(input()))

dt1 = datetime.datetime(1970, 1, 1)

dt2 = dt1 + delta

print(dt2)