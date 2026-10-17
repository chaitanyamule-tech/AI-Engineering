import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key :
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

#Prompts

prompt1 = "Hii "
prompt2 = "explain the concept of artificial intelligence in simple terms."
prompt3 = "explain the concept of artificial intelligence in simple terms, and also provide some examples of its applications in everyday life."

prompts = [prompt1, prompt2, prompt3]


for prompt in prompts:
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    usage = response.usage

    print(f"\nPrompt: {prompt}")
    print(f"Prompt tokens: {usage.prompt_tokens}")
    print(f"Completion tokens: {usage.completion_tokens}")
    print(f"Total tokens: {usage.total_tokens}")


# print(response)
print(response.choices[0].message.content)

