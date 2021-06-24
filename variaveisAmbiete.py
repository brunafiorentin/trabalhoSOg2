import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv('PASSWORD')

while True:
    var = input('\n Olá, insira o nome da Variável de Ambiente:\n')
 
    var_value = input('\n Por favor, insira o nome da Variável de Vmbiente novamente:\n')
    os.environ[var] = var_value

    print(f'\n {var}={os.environ[var]} variável de ambiente foi definida.')

    senha = input('\n Insira sua senha:\n ')
    if(senha == PASSWORD): {
        print('\n Sua senha foi aceita\n')
    }
    if (senha != PASSWORD):{
        print('\n Sua senha não foi aceita\n')
    }