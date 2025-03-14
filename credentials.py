import os
import json
from google.oauth2.service_account import Credentials

SERVICE_ACCONT_FILE = json.load(os.getenv('SERVICE_ACCONT_FILE'))

SCOPES = json.load(os.getenv('SCOPES'))

