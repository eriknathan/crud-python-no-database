from lib.interface import *
from lib.file import *
from time import sleep

arq = 'database.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Editar Pessoas', 'Excluir Pessoas', 'Sair do Menu'])

    if opcao == 1:
        listar_pessoas(arq)
    elif opcao == 2:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar_pessoa(arq, nome, idade)
    elif opcao == 3:
        nome_antigo = str(input('Nome da pessoa para editar: '))
        nova_idade = leiaInt('Nova idade da pessoa: : ')
        editar_pessoa(arq, nome_antigo, nova_idade)
    elif opcao == 4:
        nome = input("Digite o nome da pessoa que deseja excluir: ")
        excluir_pessoa(arq, nome)
    elif opcao == 5:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
