import gspread
from google.oauth2.service_account import Credentials



def conect_DB(service, scopes):

   creds = Credentials.from_service_account_file(service, scopes)
   print("credenciais")

   client = gspread.authorize(creds)
   print("autorização")

   print("abertura")
   return client.open("avisos").sheet1








