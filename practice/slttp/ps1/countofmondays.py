from datetime import datetime

year_a, year_b = input().split()

mondays = 0
months = range(1, 13)
for year in range(int(year_a), int(year_b)+1):
    for month in months:
        if datetime(year, month, 1).weekday() == 0:
            mondays += 1

print(mondays)
