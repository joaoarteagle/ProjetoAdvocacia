from datetime import datetime

# Função de Ordenar Por nome
def orderByDate(columnName, valores, database):
    print("iniciando ordenação")

    header, *dados = valores
    def convert_date(date):
      try:
         return datetime.strptime(date, '%d/%m/%Y')
      except ValueError:
         return datetime.max

    orderData = sorted(dados, key=lambda x : 
                           convert_date(x[columnName]) 
                           if len(x) > columnName 
                           else datetime.max
                     )
    print("Update dos dados")
    database.update([header] + orderData)
    print("final da ordenação")