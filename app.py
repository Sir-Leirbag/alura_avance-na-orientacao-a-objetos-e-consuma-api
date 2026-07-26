from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
