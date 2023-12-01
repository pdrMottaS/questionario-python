class MáquinaDeVendas:

    maquina = []
    count = 1

    @classmethod
    def adicionar_produto(self):
        nome = input("insira o nome do produto: ")
        valor = input("insira o valor: ")
        self.agenda.append({
            'id':self.count,
            'nome':nome,
            'valor':float(valor)
        })
        self.count += 1

    @classmethod
    def listar_produtos(self):
        for i in self.maquina:
            print(f'id: {i["id"]}\nProduto: {i["nome"]}\nValor: {i["valor"]}')

    @classmethod
    def comprar(self):
        id = input("insira o id do produto: ")
        valor = input("insira a quantidade de dinheiro: ")
        for index,i in enumerate(self.maquina):
            if i['id'] == int(id):
                if float(valor) > i['valor']:
                    troco = i['valor']-float(valor)
                    self.maquina.pop(index)
                    print(f'id: {i["id"]}\nProduto: {i["nome"]}\nValor: {i["valor"]}')
                    if troco > 0:
                        print(f'Troco: {troco}')
                else:
                    print('valor inserido menor que o valor do produto')
    
    @classmethod
    def estoque(self):
        print(f'total de produtos em estoque: {len(self.maquina)}')