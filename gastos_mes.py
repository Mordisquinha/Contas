from pynubank import Nubank
from datetime import datetime
import os 
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

nu = Nubank()
cpf = os.getenv('CPF')
senha = os.getenv('SENHA')
nu.authenticate_with_cert(cpf, senha, './cert.p12')
# print(nu.get_account_balance())

# Lista de dicionários contendo todas as transações de seu cartão de crédito
card_statements = nu.get_card_statements()
total = 0
for item in card_statements:
    hora = datetime.strptime(item['time'][:16], '%Y-%m-%dT%H:%M').strftime("%d/%m/%Y %H:%M")
    nome_estabelecimento = item['description']
    preco = str(item['amount'])
    preco = round(float(preco[:-2] + "." + preco[-2:]), 2)
    tipo = item['title']
    
    if datetime.strptime(hora, '%d/%m/%Y %H:%M').month == datetime.now().month and datetime.strptime(hora, '%d/%m/%Y %H:%M').year == datetime.now().year:
        total += item['amount']
        print('-='*30)
        print(nome_estabelecimento)
        print(preco)
        print(hora)
        print(tipo)
        print('-='*30)

total = str(total)
total = round(float(total[:-2] + "." + total[-2:]), 2)  
print(f'Gastos deste mês: {total}')
