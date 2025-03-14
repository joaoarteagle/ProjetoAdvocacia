import os
import json
from google.oauth2.service_account import Credentials

SERVICE_ACCONT_FILE = os.getenv('SERVICE_ACCONT_FILE')

SCOPES = os.getenv('SCOPES')

teste = Credentials.from_service_account_info(json.loads(SERVICE_ACCONT_FILE))

def teste():

    print(SCOPES)
    print(SERVICE_ACCONT_FILE)