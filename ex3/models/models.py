class Pessoa:

    def __init__(self,nome:str, endereco:str, cpf:int, rg:int, telefone:int):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.rg = rg
        self.telefone = telefone

    def set_nome(self,nome:str):
        self.nome = nome
    
    def get_nome(self)->str:
        return self.nome
    
    def set_endereco(self,endereco:str):
        self.endereco = endereco
    
    def get_endereco(self)->str:
        return self.endereco
    
    def set_cpf(self,cpf:int):
        self.cpf = cpf
    
    def get_cpf(self)->int:
        return self.cpf

    def set_rg(self,rg:int):
        self.rg = rg
    
    def get_rg(self)->int:
        return self.rg
    
    def set_telefone(self,telefone:int):
        self.telefone = telefone
    
    def get_telefone(self)->int:
        return self.telefone
    
class Fornecedor(Pessoa):

    def __init__(self, nome: str, endereco: str, cpf: int, rg: int, telefone: int,valor_credito:float,valor_divida:float):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.valor_credito = valor_credito
        self.valor_divida = valor_divida
    
    def obter_saldo(self)->float:
        return self.valor_credito - self.valor_divida
