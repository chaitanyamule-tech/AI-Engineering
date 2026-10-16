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
role = "user"

prompt = " Hello, Groq! How are you today?"

message ={
    "role":role,
    "content":prompt
}

message = [message]

response = client.chat.completions.create(model=model, messages=message)
print(response)
print(response.choices[0].message.content)