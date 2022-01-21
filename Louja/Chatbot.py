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
            print('4 - Fechar carrinho\n')


            escolha = input('Qual é a sua escolha? ')

            if escolha == '0':
                print('\n Este é o catálogo:')
                self.mostrarEstoque(estoque)

            elif escolha == '1':
                confirma='Sim'
                while confirma.lower() in ['s','sim']:
                    print('Escolha quantos produtos você deseja adicionar ao carrinho, seguido de qual produto, separado por espaço:\n')
                    print('(exemplo: 6 Orloff)\n')

                    produto, quantidade = self.escolhaProdutoEQuantidade(estoque)
                    if produto and quantidade:
                        carrinho.adicionaItemCarrinho(produto,quantidade,estoque)
                    else:
                        print('Não foi possível adicionar itens ao carrinho!\n')

                    print('\nDeseja adicionar mais algum item ao carrinho?\n')
                    confirma = input('Qual a sua escolha? (S/N): ')
                    while confirma.lower() not in ['sim','s','não','n','nao']:
                        print('Digite um valor válido, por favor!\n')
                        confirma = input('\nDeseja adicionar mais algum item ao carrinho? (S/N):')
                print('\n\n~~Retornando ao menu inicial~~\n\n')

            elif escolha == '2':
                confirma=str('S')
                while confirma.lower() in ['s','sim']:
                    print('Escolha quantos produtos você deseja retirar do carrinho, seguido de qual produto, separado por espaço:')
                    print('(exemplo: 3 Tang)\n')

                    produto, quantidade = self.escolhaProdutoEQuantidade(estoque)
                    if produto and quantidade:
                        carrinho.removeItemCarrinho(produto,quantidade)
                    else:
                        print('Não foi possível remover itens ao carrinho! Retornando ao menu.\n')

                    print('\nDeseja remover mais algum item do carrinho?\n')
                    confirma = input('Qual a sua escolha? (S/N): ')
                    while confirma.lower() not in ['sim','s','não','n','nao']:
                        print('Digite um valor válido, por favor!\n')
                        confirma = input('\nDeseja remover mais algum item do carrinho?(S/N):')
                print('\n\n~~Retornando ao menu inicial~~\n\n')

            elif escolha == '3':
                print('Mostrando o carrinho:\n ')
                carrinho.verCarrinho()

            elif escolha == '4':
                print('Finalizando a compra em instantes...\n')
                carrinho.fecharCarrinho(estoque)
                ativo=False
            else:
                print('Digite um valor válido (Lembre-se, é necessário digitar apenas o número da opção desejada)!\n')

    def mostrarEstoque (self,estoque):
        print(estoque)

    def escolhaProdutoEQuantidade(self,estoque):
        existeProduto=False
        compra = input('Digite sua escolha: ')
        try:
            quantidade = str()
            for i in range(0,compra.index(' ')):
                quantidade += compra[i]
    
            produtoDesejado = str()
            for i in range(compra.index(' ')+1,len(compra)):
                produtoDesejado += compra[i]
        except:
            print('\n!!!Insira os dados como requisitado!!!\n')
            return False,False

        if quantidade.isdecimal()&produtoDesejado.isalpha():
            quantidade = int(quantidade)
            for i in estoque.quantidade:
                if produtoDesejado.lower() == list(i.keys())[0].nome.lower():
                    return list(i.keys())[0],quantidade
            if not existeProduto:
                print ('Digite um produto válido! Você tentou comprar %d quantidade de %s, mas algo parece errado.\n Verifique a ortografia!'%(quantidade,produtoDesejado))
                return False,False
            
        else:
            print('Digite valores válidos! Você desejou comprar %s quantidade de %s, algo está errado.\n'%(quantidade,produtoDesejado))
            return False,False

