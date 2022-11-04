# lançar o pm no django

import requests
import csv

url = 'http://127.0.0.1:8000/plano-manut'

with open(r'C:\Users\U1106811\Documents\CsvPmAtPython.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    dados = list(reader)

for i in dados:
    myobj = {
        'ordem': i[0],
        'nota': i[1],
        'cod_local_inst': i[2],
        'local_inst': i[3],
        'tipo_insp': i[4],
        'mes': i[5],
        'status': i[6],
        'equipamento': i[7]
    }
    x = requests.post(url, json = myobj)
    print(f'OK, inserido a ordem {i[0]}')


