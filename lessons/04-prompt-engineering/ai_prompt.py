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

# prompt = " Hello, Groq! How are you today?"
complain = input("Enter the user complaint: ")

def llm_prompt(prompt):
    message = {
        "role" : "user",
        "content" : prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content
#  return response 

prompting=f"""
#ROLE:
You are a support assistant at a printing kiosk company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of three categories namely billing, technical, return.
#OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of the categories given in constraints
#Example
For instance if a user compalin says he wants a refund then the category is Return , if a user complain says he is not able to print then the category is Technical , if a user complain says he has been charged extra then the category is Billing
#FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
{complain}
"""


print(llm_prompt(prompting))