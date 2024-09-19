import os
import requests

def get_deepseek_response(message):
    # Aquí deberías implementar la lógica para comunicarte con la API de DeepSeek
    # Por ejemplo, si la API de DeepSeek tiene un endpoint para enviar mensajes:
    url = 'https://api.deepseek.com/v1/chat'
    bearer = f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"
    headers = {
        'Authorization': bearer,
        'Content-Type': 'application/json'
    }
    data = {
        'message': message
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get('response', 'No response from DeepSeek')