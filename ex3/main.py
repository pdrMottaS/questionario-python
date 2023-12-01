from services import FornecedorService,PessoaService

if __name__ == '__main__':
    pessoas = []
    while(True):
        op = input('''
            Selecione uma opcao:
              1 - Adicionar fornecedor
              2 - Adicionar pessoas
              3 - listar pessoas
              4 - obter saldo fornecedor
              5 - sair
        ''')
        if op == '1':
            nome = input('insira o nome: ')
            endereco = input('insira o endereco: ')
            cpf = input('insira o cpf: ')
            rg = input('insira o rg: ')
            telefone = input('insira o telefone: ')
            valor_credito = input('insira o valor de credito: ')
            valor_divida = input('insira o valor de divida: ')
            try:
                pessoas.append(FornecedorService.criar_fornecedor(nome,endereco,int(cpf),int(rg),int(telefone),float(valor_credito),float(valor_divida)))
            except Exception as err:
                print(err)
        elif op == '2':
            nome = input('insira o nome: ')
            endereco = input('insira o endereco: ')
            cpf = input('insira o cpf: ')
            rg = input('insira o rg: ')
            telefone = input('insira o telefone: ')
            try:
                pessoas.append(PessoaService.criar_pessoa(nome,endereco,int(cpf),int(rg),int(telefone)))
            except Exception as err:
                print(err)
        elif op == '3':
            for i in pessoas:
                print(f'Nome: {i.get_nome()}\nCPF: {i.get_cpf()}\n')
        elif op == '4':
            try:
                cpf=input('insira o cpf: ')
                for i in pessoas:
                    if i.get_cpf() == int(cpf):
                        print(i.obter_saldo())
                        break
            except Exception as err:
                print(err)
        else:
            break

