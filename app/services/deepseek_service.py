import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from app.services.chroma_service import chroma_service
load_dotenv(override=True)


def get_deepseek_response(user_message):
    
    # Realizar una consulta a ChromaDB para obtener información relevante
    chroma_results = chroma_service.query_documents(query_text=user_message, n_results=3)
    
    # Extraer los documentos relevantes de ChromaDB
    relevant_documents = [doc for doc in chroma_results['documents'][0]] if chroma_results['documents'] else []

    # Crear el mensaje para DeepSeek, incluyendo la información relevante de ChromaDB
    deepseek_message = f"{user_message}\n\nInformación relevante:\n" + "\n".join(relevant_documents)

    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
    ) 
    
    response = client.chat.completions.create(
        model='deepseek-chat',  # Specify the model
        messages=[
            {
                "role": "user", "content": deepseek_message
            }
        ],
        max_tokens=150,  # Adjust token count as needed
        temperature=0.05  # Adjust temperature for variability
    )
    
   # Acceder al contenido del mensaje generado
    assistant_message = response.choices[0].message.content
    print(f"ChatGTP: {response.choices[0].message.content}")
    return assistant_message