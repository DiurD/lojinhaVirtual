from Estoque import Estoque

class Carrinho():
    def __init__(self):
        self.produtosNoCarrinho = list()

    def adicionaItemCarrinho(self,produto,quantidadeDeCompra,estoque):
        if estoque.verificaQuantia(produto)>=quantidadeDeCompra:
            if not self.produtosNoCarrinho:
                for i in self.produtosNoCarrinho:
                    if produto is i.keys():
                        i[produto]+=quantidadeDeCompra
            else:
                self.produtosNoCarrinho.append({produto:quantidadeDeCompra})

            print('%d %s(s) adicionado(s) ao carrinho com sucesso! Feche seu carrinho rápido para evitar que outros acabem com a MEGALIQUIDAÇÃO'%(quantidadeDeCompra,produto.nome,))
        else:
            print('Só possuímos mais %d produto(s) deste, por favor compre outro produto ou espere o reabastecimento'%estoque.verificaQuantia(produto))


    def removeItemCarrinho(self,produto,quantidadeDeRemover,estoque):
        if not self.produtosNoCarrinho:
            for i in self.produtosNoCarrinho:
                if produto is i.keys():
                    if quantidadeDeRemover<=estoque.verificaQuantia(produto):
                        i[produto]-=quantidadeDeRemover
                    else:
                        print('Impossível tirar mais produtos do que seu carrinho possui!')
        else:
            print('Seu carrinho está vazio...')
 

    def verCarrinho(self):
        if not self.produtosNoCarrinho:
            print('Seu carrinho possui:\n ------------------------------\n')
            for i in self.produtosNoCarrinho:
                print('%d x %s, te custando R$ %.2f \n'%(i[list(i.keys())[0]], list(i.keys())[0].nome, list(i.keys())[0].preco))
            print('------------------------------\n')
        else:
            print('Seu carrinho está vazio...')

    def fecharCarrinho(self,estoque):
        produtosRetirados=str()
        precoTotal=float(0)
        for i in self.produtosNoCarrinho:
            for j,k in i:
                estoque.retira_produto(j,k)
                precoTotal+=j.preco
                produtosRetirados+='%d x %s, te custando R$ %.2f \n'%(k, j.nome, j.preco)
        self.produtosNoCarrinho.clear()
        print('~~~~Carrinho esvaziado com sucesso!~~~~\n')
        print('---------------NOTA FISCAL---------------\n')
        print(produtosRetirados)
        print('----VALOR FINAL: %.2f'%precoTotal)



