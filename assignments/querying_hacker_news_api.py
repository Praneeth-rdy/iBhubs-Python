import requests

response=requests.get('https://hacker-news.firebaseio.com/v0/item/' + input() + '.json')

print(response.json()['title'])