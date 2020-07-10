import requests
from bs4 import BeautifulSoup as bs
res = requests.get(input())

text =res.text

ph=bs(text)
print(ph.title.text)