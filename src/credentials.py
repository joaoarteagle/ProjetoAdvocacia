import os
import json
from google.oauth2.service_account import Credentials

json_str = os.environ.get('SERVICE_ACCONT_FILE')

if json_str is None:
    raise ValueError("Erro: A variável de ambiente 'SERVICE_ACCONT_FILE' não foi encontrada!")

print(f"Variável capturada: {json_str[:50]}...")  # Exibe apenas parte do JSON para verificar

# Agora tente carregar o JSON corretamente
SERVICE_ACCONT_FILE = json.loads(json_str)  # Usa json.loads() para strings JSON






SCOPES = json.loads(os.environ.get('SCOPES', '[]'))

# def json_to_string(file_path):
#     with open(file_path) as file:
#         print(json.dumps(json.load(file)))

# json_to_string('./resources/keys.json')

