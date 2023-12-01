from models import Pessoa

class PessoaService:

    @classmethod
    def criar_pessoa(self,nome:str, endereco:str, cpf:int, rg:int, telefone:int)->Pessoa:
        return Pessoa(nome,endereco,cpf,rg,telefone)