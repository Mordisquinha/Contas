from pynubank import Nubank
import os 
import dotenv
import random

dotenv.load_dotenv(dotenv.find_dotenv())

nu = Nubank()
cpf = os.getenv('CPF')
senha = os.getenv('SENHA')
nu.authenticate_with_cert(cpf, senha, './cert.p12')

data = nu.get_available_pix_keys()

for key in data['keys']:
    if key['kind'] == 'EVP':
        chave = key
        break
     

account_id = data['account_id'] # Retorna id da sua conta

qr = nu.create_pix_payment_qrcode(account_id, 0.01, chave)
qr = qr['qr_code']
img = qr.make_image(fill_color='black', back_color='white')

img.show()