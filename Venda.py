class Venda:


    def __init__(self, produtos,pagamento ): #produtos é uma lista de  dicionario que tem o produto e a quantidade comprada
        self.produtos = produtos
        self.pagamento = pagamento
        self._valor_compra = 0
    def __str__(self):
        return self.produtos

    @property
    def valor_compra(self):


        for produto in self.produtos:
            self._valor_compra += produto['Quantidade'] * produto['Produto'].preco

        return self._valor_compra



    def ficouFiado(self):
        if self.pagamento < self.valor_compra:
            self.fiado = True

        else:
            self.fiado = False