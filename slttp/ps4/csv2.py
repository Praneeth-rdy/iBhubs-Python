#url = https://python-courseware.s3.ap-south-1.amazonaws.com/third_party_packages/problem_sets_data/cf9f6a38-d124-4727-ba74-8607016af357.csv

import requests
import csv

response = requests.get(input())
wrapper = csv.reader(response.text.strip().split('\n'))

s=count=0
for record in wrapper:
    if count==0:
        count+=1
        continue
    s+=float(record[1])
    count+=1

print(s/(count-1))