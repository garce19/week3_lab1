import os
import requests
from dotenv import load_dotenv, find_dotenv
import autogen

# Cargar variables de entorno
load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")

llm_config = {
    "model": "gemini-1.5-flash-latest",
    "api_key": os.getenv("GOOGLE_API_KEY"),
    "api_type": "google"
}

# Obtener noticias de la API
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    meaningful_info = []

    for article in articles:
        meaningful_info.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url']
        })

    return meaningful_info

# Definir el task
task = "Write an article summarizing the latest top news in the US."

# Configurar los agentes
user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="Provide the task and send instructions to writer to refine the article.",
    code_execution_config=False,
    llm_config=llm_config,
    human_input_mode="ALWAYS",
)

planner = autogen.ConversableAgent(
    name="Planner",
    system_message="Given a task, please determine "
    "what information is needed to complete the task. "
    "Please note that all the news information will be provided by the critic. "
    "After each step is done by others, check the progress and "
    "instruct the remaining steps. If a step fails, try to workaround.",
    description="Planner. Given a task, determine what "
    "information is needed to complete the task. "
    "After each step is done by others, check the progress and "
    "instruct the remaining steps.",
    llm_config=llm_config,
)

# Obtener las noticias
news_articles = get_news()
news_context = "\n".join([f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}" for article in news_articles])

critic = autogen.ConversableAgent(
    name="Critic",
    system_message=f"You will be provided with the latest top news information in the US. Here are the articles:\n{news_context}",
    llm_config=llm_config,
)

writer = autogen.ConversableAgent(
    name="Writer",
    llm_config=llm_config,
    system_message="Writer."
    "Please write articles in markdown format (with relevant titles)"
    " and put the content in pseudo ```md``` code block. "
    "You take feedback from the admin and refine your article.",
    description="Writer."
    "Write articles based on the provided news information and take "
    "feedback from the admin to refine the article.",
)

# Simular la interacción entre agentes
groupchat = autogen.GroupChat(
    agents=[user_proxy, critic, writer, planner],
    messages=[],
    max_round=10,
    allowed_or_disallowed_speaker_transitions={
        user_proxy: [critic, writer, planner],
        critic: [planner],
        writer: [planner],
        planner: [user_proxy, critic, writer],
    },
    speaker_transitions_type="allowed",
)

manager = autogen.GroupChatManager(
    groupchat=groupchat, llm_config=llm_config
)

# Iniciar el chat con la tarea
groupchat_result = user_proxy.initiate_chat(
    manager,
    message=task
)

#print(groupchat_result)
