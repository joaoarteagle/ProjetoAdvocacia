import gspread
from google.oauth2.service_account import Credentials
from orderByDate import orderByDate
from apresenta import apresenta



def conect_DB(service, scopes):

   creds = Credentials.from_service_account_file(filename = service, kwargs = scopes)
   print("credenciais")

   client = gspread.authorize(creds)
   print("autorização")

   print("abertura")
   return client.open("avisos").sheet1








