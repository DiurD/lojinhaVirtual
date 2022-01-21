from Carrinho import Carrinho
from Estoque import Estoque

class ChatBot():
    def menu(self,carrinho,estoque):
        ativo= True
        while ativo:
            print('======== Digite o número da ação que você deseja realizar: ========\n ')
            print('0 - Mostrar catálogo da loja')
            print('1 - Adicionar item ao carrinho')
            print('2 - Remover item do carrinho')
            print('3 - Mostrar items do carrinho')
            print('4 - Fechar carrinho')


            escolha = input('Qual é a sua escolha?')

            if escolha == '0':
                print('Este é o catálogo:\n ')
                self.mostrarEstoque(estoque)
            elif escolha is '1':
                produto, quantidade = self.escolhaProdutoEQuantidade(estoque)

            elif escolha is '2':
                print('Este é o catálogo ')

            elif escolha is '3':
                print('Este é o catálogo ')

            elif escolha is '4':
                print('')

            else:
                print('Digite um valor válido (Lembre-se, é necessário digitar apenas o número da opção desejada)!')

    def mostrarEstoque (self,estoque):
        print(estoque)

    def escolhaProdutoEQuantidade(self,estoque):
        print('Escolha quantos produtos, seguido de qual produto, separado por espaço:\n')
        print('(exemplo: 6 Vodka\n')
        compra = input('Digite sua escolha:')
        quantidade = compra.split(' ')[0]
        produtoDesejado = compra.split(' ')[1]
        if quantidade.isdecimal()&produtoDesejado.isalpha():
            for i in estoque:

                quantidade = int(quantidade)
            return produto,qt
        else:
            print('Digite valores válidos!')
            return False

