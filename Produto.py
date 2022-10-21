class Produto:
    def __init__(self, nome, preco, estoque, categoria):
        self.nome = nome
        self._preco = preco
        self.estoque = estoque
        self.categoria = categoria

    def __str__(self):
        return self.nome

    @property
    def preco(self):
        return  self._preco

    @preco.setter
    def preco(self, preco):
        if preco<0:
            print('O preço não pode ser negativo')
        else:
            self._preco = preco




