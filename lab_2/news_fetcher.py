import requests
import os

API_KEY = os.environ["API_KEY"]
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)

articles = data['articles']
meaningful_info = []

for article in articles:
    meaningful_info.append({
        'title': article['title'],
        'description': article['description'],
        'url': article['url']
    })

# Guarda la información significativa en un archivo
with open('./news_data.txt', 'w', encoding='utf-8') as f:
    for info in meaningful_info:
        f.write(f"Title: {info['title']}\n")
        f.write(f"Description: {info['description']}\n")
        f.write(f"URL: {info['url']}\n\n")
