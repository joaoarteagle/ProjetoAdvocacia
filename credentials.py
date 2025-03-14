import os
import json
from google.oauth2.service_account import Credentials

SERVICE_ACCONT_FILE = Credentials.from_service_account_info(json.loads(os.getenv('SERVICE_ACCONT_FILE')))

SCOPES = json.loads(os.getenv('SCOPES'))

