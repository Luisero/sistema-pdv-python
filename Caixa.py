from Venda import Venda
from Veaco import Veaco
from clear import clear


class Caixa:
    produtos = []
    categorias = []
    clientes = []
    vendas = []
    veacos = []
        
    def __init__(self, dinheiro_caixa):
        self.dinheiro_caixa = dinheiro_caixa


    def get_categorias(self):
        texto_categoria = ''
        for i, categoria in enumerate(self.categorias):
            texto_categoria += f'[{i}]-Categoria: {categoria.categoria}\n'

        return texto_categoria
    

    def get_produtos(self):
        texto_produto = ''
        for i, produto in enumerate(self.produtos):
            texto_produto += f'[{i}]-Produto: {produto.nome} Categoria: {produto.categoria} Estoque: {produto.estoque}\n'

        return texto_produto

    def get_produto(self, id_produto):
        produto = self.produtos[id_produto]
        return  f'[{id_produto}]-Produto: {produto.nome} Categoria: {produto.categoria} Estoque: {produto.estoque}\n'

    def adicionar_estoque(self, id_produto, nova_quantidade):
        self.produtos[id_produto].estoque = nova_quantidade

    def adicionar_produto(self, produto):
        self.produtos.append(produto)


    def realizarVenda(self):
        
        clear()
        print(self.get_clientes())
        id_cliente = int(input('Digite o id do cliente: '))

        cliente = self.clientes[id_cliente]
        print(self.get_produtos())

        carrinho = []

        escolha_comprar = '0'

        while escolha_comprar == '0':
            id_produto = int(input('Digite o id do produto: '))
            print(self.get_produto(id_produto))
            produto = self.produtos[id_produto]
            quantidade = input(f'Quantos {produto.nome} quer comprar? ')
            
            carrinho.append({"Produto":produto,"Quantidade": quantidade})

            escolha_comprar = input('Quer adicionar outro produto ao carrinho? [0]Sim [1]Não ')

            if escolha_comprar == '1':
                break

        valor_pagamento = float(input('Digite o valor com que quer pagar'))

        venda = Venda(carrinho,valor_pagamento,cliente)

        if venda.ficouFiado():
            veaco = Veaco(cliente, venda.valorFiado())
            self.veacos.append(veaco)
        self.vendas.append(venda)

    def get_veacos(self):
        texto_veacos= ''

        for veaco in self.veacos:
            print(veaco)
    def get_vendas(self):
        texto_vendas = ''

        for venda in self.vendas:
            
            for produto in venda.produtos:
                produto_vendido = produto['Produto']

                texto_vendas += f'| Produto {produto["Produto"]} - Quantidade: {produto["Quantidade"]} | Valor: |'

            texto_vendas += f'| R$ {venda.valor_compra}\n'

        return texto_vendas

    def get_clientes(self):
        texto_clientes = ''

        for i, cliente in enumerate(self.clientes):
            texto_clientes += f'[{i}] Cliente: {cliente.nome}\n'



        return texto_clientes


