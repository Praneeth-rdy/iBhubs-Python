import datetime

dt_format = "%a %d %b %Y %H:%M:%S"
input_dt = datetime.datetime.strptime(input(), dt_format)
ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
ist_dt = input_dt.astimezone(tz=ist_tz)
print(ist_dt.strftime(dt_format))