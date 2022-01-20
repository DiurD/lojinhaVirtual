from os import name
from Produtos import Produto

class Estoque():
    def __init__(self):
        self.quantidade=list()

    def adicionaProduto (self,produto,quantidade):
        self.quantidade.append({produto:quantidade})
    
    def retira_produto(self,produto,quantidade):
        achou=False
        for i in self.quantidade:
            if produto in i.keys():
                if i[produto]-quantidade>=0:
                    i[produto]-=quantidade
                    print('%d produto(s) retirado(s) da prateleira com sucesso! Temos apenas mais %d produtos %s'%(quantidade,i[produto],list(i.keys())[0].nome))
                else:
                    print('Só possuímos mais %d produto(s) deste, por favor compre outro produto ou espere o reabastecimento'%i[produto])
                achou=True

        if not achou:     
            print('Não foi possível achar o produto')

    def __str__(self):
        catalogo=str()
        for i in self.quantidade:
            catalogo += '%d x %s (R$ %.2f) \n'%(i[list(i.keys())[0]], list(i.keys())[0].nome, list(i.keys())[0].preco)
        return catalogo

