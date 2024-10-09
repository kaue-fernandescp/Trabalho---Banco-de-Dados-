from tabela import Tabela

pessoas = Tabela()

valor = True
while valor:
    print('''
        1 - Criar tabela
        2 - Inserir
        3 - Alterar
        4 - Deletar
        5 - Ler
        6 - Sair
    ''')
    opcao = int(input('Escolha uma das opções acima: '))
    if opcao == 1:
        pessoas.criar_tabela()
    elif opcao == 2:
        nome = input('Insira o nome: ')
        cpf = input('Insira o CPF: ')
        pessoas.inserir(nome, cpf)
    elif opcao == 3:
        id = int(input('Qual id você quer alterar? '))
        nome = input('Insira o novo nome: ')
        cpf = input('Insira o novo CPF: ')
        pessoas.alterar(id, nome, cpf)
    elif opcao == 4:
        id = int(input('Qual id você quer deletar? '))
        pessoas.deletar(id)
    elif opcao == 5:
        print(pessoas.selecionar())
    elif opcao == 6:
        valor = False
        pessoas.fechar()