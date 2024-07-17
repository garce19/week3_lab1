import google.generativeai as genai
from dotenv import load_dotenv
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

#response = model.generate_content("Write a story about a AI and magic")
#print(response.text)


# Definir los diferentes tipos de prompts
prompts = {
    "Few-shot": """
Q: What is the capital of France?
A: Paris.

Q: What is the largest mammal?
A: The blue whale.

Q: Who wrote Hamlet?
A: William Shakespeare.

Q: How does AI learn?
A:""",
    "CoT": """
Q: How many seconds are in a year?
A: Think step by step. There are 60 seconds in a minute...""",
    "Prompt Chain": """
Q: What is AI?
A: AI, or Artificial Intelligence, is...

Q: How does AI impact daily life?
A:""",
    "Self-Consistency Prompting": """
Q: What is the best way to ensure a fair election?
A1: Ensuring a fair election can be achieved by...
A2: One method to guarantee fairness in elections is...
A3: A fair election is best ensured by..."""

}

# Función para enviar prompts y guardar las respuestas
def send_prompt_and_save(prompt_type, prompt_text):
    response = model.generate_content(prompt_text)
    print(f"Prompt Type: {prompt_type}\nPrompt:\n{prompt_text}\nResponse:\n{response.text}\n")
    with open(f"{prompt_type}_response.md", "w") as file:
        file.write(f"## Prompt Type: {prompt_type}\n### Prompt:\n{prompt_text}\n### Response:\n{response.text}\n")

# Enviar cada prompt a la API, imprimir y guardar la respuesta
for prompt_type, prompt_text in prompts.items():
    send_prompt_and_save(prompt_type, prompt_text)