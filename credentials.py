import os
import json

SERVICE_ACCONT_FILE = os.getenv('SERVICE_ACCONT_FILE')

SCOPES = os.getenv('SCOPES')


def teste():

    print(SCOPES)
    print(SERVICE_ACCONT_FILE)