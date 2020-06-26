#url = https://python-courseware.s3.ap-south-1.amazonaws.com/third_party_packages/problem_sets_data/cf9f6a38-d124-4727-ba74-8607016af357.csv


import requests
import csv

url = input()
name=input()
response = requests.get(url)

wrapper = csv.reader(response.text.strip().split('\n'))

for record in wrapper:
    if record[0]==name:
        print(record[1])
    