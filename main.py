from Cliente import Cliente
from Categorias import Categoria
from Produto import Produto
from Venda import Venda
from Mercado import Mercado

clientes = [
    Cliente('Vivy', 9812345),
    Cliente('Luis',9787458)
]

categorias = [
    Categoria('Laticíneos'),
    Categoria('Cereais'),
    Categoria('Grãos'),
    Categoria('Limpeza'),
    Categoria('Maromba')
]

produtos = [
    Produto('Sabão em pó da OMO', 8, 15, categorias[3]),
    Produto('Barra de proteínas', 3, 20, categorias[4]),
    Produto('Arroz', 4,10, categorias[1]),
    Produto('Feijão',  8, 15, categorias[2])
]

vendas = [
    Venda([{'Produto':produtos[3], 'Quantidade':4}], 50)
]

#
# for produto in vendas[0].produtos:
#     print(produto['Produto'])
#     print(produto['Quantidade'])




