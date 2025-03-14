from connectionSheets import conect_DB
from apresenta import apresenta
from orderByDate import orderByDate
from credentials import *



def main(accont, scopes):
        
    DATABASE = conect_DB(service = accont, scopes = scopes )
    data = DATABASE.get_all_records()
    apresenta(data)
    orderByDate(3, valores=DATABASE.get_all_values(), database=DATABASE)





main(accont = SERVICE_ACCONT_FILE, scopes = SCOPES)
