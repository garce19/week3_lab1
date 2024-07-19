import requests
from autogen import GroupChat, UserProxy, Critic, Writer, Planner
import os

API_KEY = os.environ["API_KEY"]
URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + API_KEY

response = requests.get(URL)
news_data = response.json()

# Assuming we want to concatenate the titles and descriptions of the top news to form the input data
news_texts = [f"{item['title']}. {item['description']}" for item in news_data['articles']]
input_data = ' '.join(news_texts)

# Configura los agentes
user_proxy = UserProxy(input_data)
critic = Critic()
writer = Writer()
planner = Planner()

# Crea un GroupChat
group_chat = GroupChat([user_proxy, critic, writer, planner])

# Genera el artículo
article = group_chat.generate_article()

# Guarda el artículo en un archivo con codificación utf-8
with open('./lab_2/generated_article.txt', 'w', encoding='utf-8') as f:
    f.write(article)