import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)


def get_deepseek_response(user_message):
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
    ) 
    
    response = client.chat.completions.create(
        model='deepseek-chat',  # Specify the model
        messages=[
            {
                "role": "user", "content": user_message
            }
        ],
        max_tokens=150,  # Adjust token count as needed
        temperature=0.1  # Adjust temperature for variability
    )
    
    assistant_message = response.choices[0].message.content  # Access the generated message content
    print(f"ChatGTP: {response.choices[0].message.content}")
    return assistant_message
