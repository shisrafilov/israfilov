import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')

json = r.json()
answer = []

for i in json:
    answer.append({i['id'], i['title']})

print(answer)
