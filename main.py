from Cliente import Cliente
from Categorias import Categoria
from Produto import Produto
from Venda import Venda
from Caixa import Caixa
from Veaco import Veaco
from clear import clear
from time import sleep

caixa = Caixa(100)

caixa.clientes = [
    Cliente('Vivy'),
    Cliente('Luis')
]

caixa.categorias = [
    Categoria('Laticíneos'),
    Categoria('Cereais'),
    Categoria('Grãos'),
    Categoria('Limpeza'),
    Categoria('Maromba')
]

caixa.produtos = [
    Produto('Sabão em pó da OMO', 8, 15, caixa.categorias[3]),
    Produto('Barra de proteínas', 3, 20, caixa.categorias[4]),
    Produto('Arroz', 4,10, caixa.categorias[1]),
    Produto('Feijão',  8, 15, caixa.categorias[2])
]

caixa.vendas = [
    Venda([{'Produto':caixa.produtos[3], 'Quantidade':4}], 50, caixa.clientes[0]),
    Venda([{'Produto':caixa.produtos[2], 'Quantidade': 4}, {'Produto':caixa.produtos[1], 'Quantidade':4}],100, caixa.clientes[1])
]


# for produto in caixa.vendas[0].produtos:
#     print(produto['Produto'])
#     print(produto['Quantidade'])

def main():
    while True:
        clear()
        print(f'+{"":-^25.25}+')
        print(f'|{"Cadastrar cliente [0]": ^25.25}|')
        print(f'|{"Cadastrar produto [1]": ^25.25}|')
        print(f'|{"Checar estoques [2]": ^25.25}|')
        print(f'|{"Realizar venda [3]": ^25.25}|')
        print(f'|{"Checar vendas [4]": ^25.25}|')
        print(f'|{"Checar veacos [5]": ^25.25}|')
        print(f'+{"":-^25.25}+')

        escolha = input('O que deseja fazer?')

        #cadastrar cliente
        if escolha == '0':
            nome = input('Digite o nome do cliente: ')

            cliente = Cliente(nome)

            caixa.clientes.append(cliente)
            clear()

            print('Cliente cadastrado.')
            sleep(1)
        #cadastrar produto
        elif escolha == '1':
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o preço do produto: '))
            quantidade = int(input('Digite a quantidade do produto: '))

            clear()
            print(caixa.get_categorias())
            id_categoria = int(input('Qual o  índice da categoria do produto?'))

            categoria = caixa.categorias[id_categoria]

            produto = Produto(nome, preco, quantidade, categoria)

            caixa.adicionar_produto(produto)
            
            clear()

            print(caixa.get_produtos())

            print('\n Produto adicionado.')

            sleep(1)

        #mudar estoque
        elif escolha == '2':

            clear()

            print(caixa.get_produtos())

            input('Adicionar estoque de produtos? [0] Sim [1] Não: ')

            if escolha == '1':
                pass 
            else:
                clear()

                print(caixa.get_produtos())

                id_produto = int(input('Qual o id do produto? '))

                clear()

                print(caixa.get_produto(id_produto))
                
                novo_estoque = int(input('Digite a nova quantidade '))

                caixa.adicionar_estoque(id_produto, novo_estoque)

                clear()

                print('Produto atualizado.')
                sleep(1)

        #realizar venda
        elif escolha == '3':
            caixa.realizarVenda()


        #checar vendas
        elif escolha == '4':
            print(caixa.get_vendas())
            input('Enter para sair')
            clear()

        #checar veacos
        elif escolha == '5':
            caixa.get_veacos()
main()
