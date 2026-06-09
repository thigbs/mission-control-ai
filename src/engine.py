import os
from dotenv import load_dotenv
from src.telemetria import coletar
from src.alertas import avaliar
import requests

load_dotenv()

def executar_missao():
    dados = coletar()
    alertas = avaliar(dados)
    return dados, alertas


def analisar_com_ia(dados, alertas):

    url = "https://ollama.com/api/chat"

    headers = {
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-oss:120b",
        "messages": [
            {
                "role": "system",
                "content": "Você é um especialista em satélites agrícolas."
            },
            {
                "role": "user",
                "content": f"DADOS: {dados}\nALERTAS: {alertas}"
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)
    print(response.text)

    return "Teste concluído"
