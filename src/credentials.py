import os
import json
from google.oauth2.service_account import Credentials

SERVICE_ACCONT_FILE = json.load(os.environ.get('SERVICE_ACCONT_FILE'))

SCOPES = json.load(os.environ.get('SCOPES'))

def json_to_string(file_path):
    with open(file_path) as file:
        print(json.dumps(json.load(file)))

json_to_string('./resources/keys.json')