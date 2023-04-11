from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def listar_pessoas(nome, info):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        if info.st_size == 0:
            print('Não há pessoas cadastradas')
        else:
            cabeçalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<10}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar_pessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um [ERRO] na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Pessoa: {nome} | Cadastrada com sucesso!')
            a.close()


def editar_pessoa(arq, nome_antigo, nova_idade):
    try:
        a = open(arq, 'r')
        pessoas = []
        for linha in a:
            nome, idade = linha.strip().split(";")
            if nome == nome_antigo:
                pessoas.append(f"{nome};{nova_idade}\n")
            else:
                pessoas.append(f"{nome};{idade}\n")
        a = open(arq, 'w')
        a.writelines(pessoas)
    except:
        print('Houve um [ERRO] na edição do arquivo')
    else:
        print("Pessoa EDITADA com sucesso!")


def excluir_pessoa(arq, nome):
    try:
        a = open(arq, 'r')
        pessoas = []
        for linha in a:
            nome_pessoa, _ = linha.strip().split(";")
            if nome != nome_pessoa:
                pessoas.append(linha)
        a.close()
        a = open(arq, 'w')
        a.writelines(pessoas)
        a.close()
    except:
        print('Houve um [ERRO] ao excluir a pessoa')
    else:
        print("Pessoa EXCLUÍDA com sucesso!")