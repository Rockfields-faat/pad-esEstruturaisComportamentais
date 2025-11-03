from .estrategias import EstrategiaPagamento, EstrategiaFrete
from .decoradores import CalculoValor
from .subsistemas import SistemaEstoque, GeradorNotaFiscal

class CheckoutFacade:
    def __init__(self, estrategia_pagamento: EstrategiaPagamento, estrategia_frete: EstrategiaFrete):
        self.estoque = SistemaEstoque()
        self.nota_fiscal = GeradorNotaFiscal()
        self.estrategia_pagamento = estrategia_pagamento
        self.estrategia_frete = estrategia_frete

    def concluir_transacao(self, calculo_valor: CalculoValor):
        print("=========================================")
        print("INICIANDO CHECKOUT...")
        valor = calculo_valor.calcular()
        custo_frete = self.estrategia_frete.calcular_frete(valor)
        valor_final = valor + custo_frete
        print(f"Valor final com frete: R${valor_final:.2f}")
        if self.estrategia_pagamento.processar_pagamento(valor_final):
            self.estoque.registrar_pedido()
            self.nota_fiscal.emitir_nota()
            print("SUCESSO: Pedido finalizado.")
        else:
            print("FALHA: Transação abortada.")
