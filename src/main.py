from functions.data_function.connectionSheets import conect_DB
from functions.data_function.apresenta import apresenta
from functions.data_function.orderByDate import orderByDate
from credentials import *
from fastapi import FastAPI
from mangum import Mangum

def main(accont, scopes):
        
    DATABASE = conect_DB(service = accont, scopes = scopes )
    data = DATABASE.get_all_records()
    apresenta(data)
    orderByDate(3, valores=DATABASE.get_all_values(), database=DATABASE)

app = FastAPI()



@app.get("/")
def home(event, context):
    
    try:
        main(accont = SERVICE_ACCONT_FILE, scopes = SCOPES)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Automação rodando"})
        }
    except Exception as e:
        return{
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    

handler = Mangum(app)