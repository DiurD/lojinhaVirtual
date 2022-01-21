from Produtos import Produto #Retirar no futuro
from Estoque import Estoque #Retirar no futuro
from Chatbot import ChatBot
from Carrinho import Carrinho

if __name__ == "__main__":

        Cachaça = Produto('Cachaça',2.5)
        Suco = Produto('Suco',6.50)
        Miojo = Produto('Miojo',0.7)
        Vodka = Produto('Orloff',24.90)
        SapoDourado = Produto ('Sapo dourado',420.69)
        MaçoCigarro = Produto('Maço de cigarro',19.9)

        Stok = Estoque()
        Stok.adicionaProduto(Cachaça,10)
        Stok.adicionaProduto(Suco,5)
        Stok.adicionaProduto(Vodka,10)
        Stok.adicionaProduto(Miojo,10)
        Stok.adicionaProduto(SapoDourado,1)
        Stok.adicionaProduto(MaçoCigarro,15)

        print('Bem vindx à mercearia virtual da UFMG! Estes são nossos produtos:')
        print(Stok)

        CarrinhoDoNovoCliente=Carrinho()
        NovoChat= ChatBot()

        NovoChat.menu(CarrinhoDoNovoCliente,Stok)

        print('\n~~Obrigado por fazer negócios conosco!~~\n')






