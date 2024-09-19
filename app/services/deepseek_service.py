import os
import requests
from dotenv import load_dotenv
load_dotenv()

def get_deepseek_response(user_message):
    # Aquí deberías implementar la lógica para comunicarte con la API de DeepSeek
    # Por ejemplo, si la API de DeepSeek tiene un endpoint para enviar mensajes:
    url = "https://api.deepseek.com/chat/completions"
    bearer = f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"
    headers = {
        'Authorization': bearer,
        'Content-Type': 'application/json'
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    
    try:
        response_json = response.json()
        print("Full response:", response_json)  # Imprime la respuesta completa
        if 'choices' in response_json and len(response_json['choices']) > 0:
            assistant_message = response_json['choices'][0]['message']['content']
            return assistant_message
        else:
            return "No response from DeepSeek"

    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response content: {response.text}")
        return "Error decoding JSON"