import time
import os

from lib.interface import cabeçalho
from lib.sistema import sistema
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

usuario_correto = os.getenv('USUARIO_CORRETO')
senha_correta = os.getenv('SENHA_CORRETA')


def fazerLogin():
    cabeçalho('ENTRAR NO SISETEMA')
    login = str(input('Login: '))
    password = str(input('Senha: '))
    if login == usuario_correto and password == senha_correta:
        print('Acessando sistema...')
        time.sleep(2)
        sistema()
    else:
        print('Acesso Negado!')
        return fazerLogin()
