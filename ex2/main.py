from models import Livro, Mouse

if __name__=='__main__':
    carrinho = []

    mouse_mock = Mouse('loja 1',10.0,'Mouse ótico, Saída USB. 1.600 dpi')
    carrinho.append(mouse_mock)
    livro_mock = Livro('loja 1',16.0,'Clarisse Lispector')
    carrinho.append(livro_mock)

    for item in carrinho:
        print(item.get_descricao())