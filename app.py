from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_brigadeiro = Sobremesa('Brigadeiro', 5.0, 'Chocolate', 'Médio', 'Feito com chocolate artesanal')
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_brigadeiro)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
