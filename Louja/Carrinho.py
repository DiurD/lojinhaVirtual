from Estoque import Estoque

class Carrinho():
    def __init__(self):
        self.produtosNoCarrinho = list()

    def adicionaItemCarrinho(self,produto,quantidadeDeCompra,estoque):
        print ('\nQuantidade em estoque:' + str(estoque.verificaQuantia(produto)))
        print ('Quantidade desejada:' + str(quantidadeDeCompra))
        quantidadeNoCarrinho =0

        for i in self.produtosNoCarrinho:
            if produto in i.keys():
                quantidadeNoCarrinho = i[produto]

        print ('Quantidade no carrinho:' + str(quantidadeNoCarrinho))


        if estoque.verificaQuantia(produto)>=(quantidadeDeCompra+quantidadeNoCarrinho):
            if self.produtosNoCarrinho:
                for i in self.produtosNoCarrinho:
                    if produto in i.keys():
                        i[produto]+=quantidadeDeCompra
                        return
                    elif produto not in i.keys(): 
                        self.produtosNoCarrinho.append({produto:quantidadeDeCompra})
                        return
                        
            else:
                self.produtosNoCarrinho.append({produto:quantidadeDeCompra})
            print('\n %d %s(s) adicionado(a)(s) ao carrinho com sucesso! Feche seu carrinho rápido para evitar que outros não acabem com seu produto!'%(quantidadeDeCompra,produto.nome,))
        else:
            print('\n Só possuímos %d produto(s) deste, por favor compre outro produto ou espere o reabastecimento'%estoque.verificaQuantia(produto))


    def removeItemCarrinho(self,produto,quantidadeDeRemover):
        if self.produtosNoCarrinho:
            for i in self.produtosNoCarrinho:
                if produto in i.keys():
                    if quantidadeDeRemover<=i[produto]:
                        i[produto]-=quantidadeDeRemover
                        print ('\n %d %s(s) removidos do carrinho com sucesso!\n'%(quantidadeDeRemover,produto.nome))
                        return
                    else:
                        print('\nImpossível tirar mais produtos do que seu carrinho possui!')
        else:
            print('\n Seu carrinho está vazio...\n')
 

    def verCarrinho(self):
        if self.produtosNoCarrinho:
            print('\nSeu carrinho possui:\n ------------------------------\n')
            for i in self.produtosNoCarrinho:
                print('%d x %s(s), te custando R$ %.2f \n'%(i[list(i.keys())[0]], list(i.keys())[0].nome, list(i.keys())[0].preco*i[list(i.keys())[0]]))
            print('------------------------------\n')
        else:
            print('Seu carrinho está vazio...\n')

    def fecharCarrinho(self,estoque):
        if  self.produtosNoCarrinho:
            produtosRetirados=str()
            precoTotal=float(0)
            for i in self.produtosNoCarrinho:
                estoque.retira_produto(list(i.keys())[0],i[list(i.keys())[0]])
                precoTotal+=list(i.keys())[0].preco*i[list(i.keys())[0]]
                produtosRetirados+='%d x %s(s), te custando R$ %.2f \n'%(i[list(i.keys())[0]], list(i.keys())[0].nome, list(i.keys())[0].preco*i[list(i.keys())[0]])
            self.produtosNoCarrinho.clear()
            print('~~~~Compra realizada com sucesso!~~~~\n')
            print('---------------NOTA FISCAL---------------\n')
            print(produtosRetirados)
            print('----VALOR FINAL: %.2f'%precoTotal)
        else:
            print('Seu carrinho está vazio, encerrando o aplicativo mesmo assim...\n')



