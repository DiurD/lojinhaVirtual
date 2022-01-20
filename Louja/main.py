from Produtos import Produto
from Estoque import Estoque

if __name__ == "__main__":
        Barrigudinha = Produto('Cachaça',2.5)
        Suco = Produto('Suco',0.5)
        Miojo = Produto('Miojo Nissin',0.7)
        Vodka = Produto('Orloff',24.90)
        Stok = Estoque()
        Stok.adicionaProduto(Barrigudinha,10)
        Stok.adicionaProduto(Suco,5)
        Stok.adicionaProduto(Vodka,10)
        Stok.adicionaProduto(Miojo,10)
        Stok.retira_produto(Suco,6)
        print(Stok)




