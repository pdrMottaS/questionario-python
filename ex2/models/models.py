class Produto:

    def __init__(self,nomeloja:str,preco:float):
        self.nomeloja = nomeloja
        self.preco = preco

    def set_nomeloja(self,nomeloja:str):
        self.nomeloja = nomeloja
    
    def set_preco(self,preco:float):
        self.preco = preco
    
    def get_nomeloja(self)->str:
        return self.nomeloja
    
    def get_preco(self)->str:
        return self.preco
    
    def get_descricao()->str:
        return "Produto de informática"
    
class Mouse(Produto):

    def __init__(self,nomeloja:str,preco:float,descricao:str):
        super().__init__(nomeloja,preco)
        self.descricao = descricao
        self.prefix = "tipo"

    def get_descricao(self) -> str:
        return f'{self.prefix}: {self.descricao}'

class Livro(Produto):

    def __init__(self,nomeloja:str,preco:float,descricao:str):
        super().__init__(nomeloja,preco)
        self.descricao = descricao
        self.prefix = "autor"

    def get_descricao(self) -> str:
        return f'{self.prefix}: {self.descricao}'
    
