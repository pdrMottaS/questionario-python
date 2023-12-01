from abc import abstractmethod

class Pessoa:

    def __init__(self, nome:str, endereco:str, valor_pagamento:float, contato:list[str]):
        self.nome = nome
        self.endereco = endereco
        self.valor_pagamento = valor_pagamento
        self.contato = contato

    @abstractmethod
    def realizar_pagamento()->float:
        pass

class PessoaFisica(Pessoa):

    def __init__(self,nome:str, endereco:str, valor_pagamento:float, contato:list[str],cpf:int,imposto:float = 0.10):
        super().__init__(nome,endereco,valor_pagamento,contato)
        self.cpf = cpf
        self.imposto = imposto

    def realizar_pagamento(self)->float:
        return self.valor_pagamento(self.valor_pagamento*self.imposto)
    
class PessoaFisica(Pessoa):

    def __init__(self,nome:str, endereco:str, valor_pagamento:float, contato:list[str],cnpj:int,nome_fantasia:str,razao_social:str,imposto:float = 0.20):
        super().__init__(nome,endereco,valor_pagamento,contato)
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.imposto = imposto

    def realizar_pagamento(self)->float:
        return self.valor_pagamento(self.valor_pagamento*self.imposto)

    
