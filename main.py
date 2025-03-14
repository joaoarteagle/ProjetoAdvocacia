from connectionSheets import conect_DB
from apresenta import apresenta
from orderByDate import orderByDate

SERVICE_ACCONT_FILE = "./resources/projetoadvocacia-444317-3e540d06f0be.json"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]



def main(accont, scopes):
        
    DATABASE = conect_DB(SERVICE_ACCONT_FILE = accont, SCOPES = scopes )
    data = DATABASE.get_all_records()
    apresenta(data)
    orderByDate(3, valores=DATABASE.get_all_values(), database=DATABASE)





main(accont = SERVICE_ACCONT_FILE, scopes = SCOPES)