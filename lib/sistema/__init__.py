from lib.file import cadastrar_pessoa, editar_pessoa,\
    excluir_pessoa, listar_pessoas
from lib.interface import leiaInt, cabeçalho, menu
from lib.createfile import criarArquivo, arquivoExiste
from time import sleep

import os

arq = 'database/database.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


def sistema():
    while True:
        opcao = menu([
            'Ver pessoas cadastradas',
            'Cadastrar Pessoas',
            'Editar Pessoas',
            'Excluir Pessoas',
            'Sair do Menu'])

        # LISTAR PESSOAS
        if opcao == 1:
            # OBTENDO INFORMAÇÃO SOBRE O ARQUIVO
            info = os.stat(arq)
            listar_pessoas(arq, info)
        # CADASTRAR PESSOAS
        elif opcao == 2:
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar_pessoa(arq, nome, idade)
        # EDITAR PESSOAS
        elif opcao == 3:
            nome_antigo = str(input('Nome da pessoa para editar: '))
            nova_idade = leiaInt('Nova idade da pessoa: ')
            editar_pessoa(arq, nome_antigo, nova_idade)
        # EXCLUIR PESSOAS
        elif opcao == 4:
            nome = input("Digite o nome da pessoa que deseja excluir: ")
            excluir_pessoa(arq, nome)
        # SAIR DO SISTEMA
        elif opcao == 5:
            cabeçalho('Saindo do sistema... Até logo!')
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1.5)
