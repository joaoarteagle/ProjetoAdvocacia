import gspread
from google.oauth2.service_account import Credentials
from orderByDate import orderByDate
from apresenta import apresenta



def conect_DB(SERVICE_ACCONT_FILE, SCOPES):

   creds = Credentials.from_service_account_file(SERVICE_ACCONT_FILE,SCOPES)
   print("credenciais")

   client = gspread.authorize(creds)
   print("autorização")

   print("abertura")
   return client.open("avisos").sheet1








