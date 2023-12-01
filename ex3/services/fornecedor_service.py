from models import Fornecedor

class FornecedorService:

    @classmethod
    def criar_fornecedor(self,nome: str, endereco: str, cpf: int, rg: int, telefone: int,valor_credito:float,valor_divida:float)->Fornecedor:
        return Fornecedor(nome,endereco,cpf,rg,telefone,valor_credito,valor_divida)
