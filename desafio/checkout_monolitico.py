from .estrategias import PagamentoPix, PagamentoCredito, FreteNormal, FreteExpresso
from .decoradores import ValorBase, DescontoPix, TaxaEmbalagemPresente
from .checkout_facade import CheckoutFacade

if __name__ == "__main__":
    valor_base = ValorBase(230.0)
    valor_com_desconto = DescontoPix(valor_base)
    checkout = CheckoutFacade(PagamentoPix(), FreteNormal())
    checkout.concluir_transacao(valor_com_desconto)

    print("\n--- Próximo Pedido ---")

    valor_base = ValorBase(600.0)
    valor_com_taxa = TaxaEmbalagemPresente(valor_base)
    checkout = CheckoutFacade(PagamentoCredito(), FreteExpresso())
    checkout.concluir_transacao(valor_com_taxa)