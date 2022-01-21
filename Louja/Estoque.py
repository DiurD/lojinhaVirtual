from Produtos import Produto

class Estoque():
    def __init__(self):
        self.quantidade=list()

    def adicionaProduto (self,produto,quantidade):
        self.quantidade.append({produto:quantidade})
    
    def verificaQuantia(self,produto):
        for i in self.quantidade:
            if produto in i.keys():    
                return i[produto]

    def verificaProduto(self,produto):
        for i in self.quantidade:
            if produto in i.keys():    
                return list(i.keys())[0]
        return False

    def retira_produto(self,produto,quantidade):
        for i in self.quantidade:
            if produto in i.keys():
                if i[produto]-quantidade>=0:
                    i[produto]-=quantidade
                    print('%d produto(s) retirado(s) da prateleira com sucesso! Temos apenas mais %d produtos %s'%(quantidade,i[produto],list(i.keys())[0].nome))
                else:
                    print('-> Produto indisponível ou acabou antes do fechamento do seu carrinho!\n Só possuímos mais %d produto(s) deste, por favor compre outro produto ou espere o reabastecimento'%i[produto])
                

    def __str__(self):
        catalogo='------------------------------------\n'
        for i in self.quantidade:
            catalogo += '%d x %s (R$ %.2f cada) \n'%(i[list(i.keys())[0]], list(i.keys())[0].nome, list(i.keys())[0].preco)
        catalogo+='------------------------------------'
        return catalogo

