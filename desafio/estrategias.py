from abc import ABC, abstractmethod

class EstrategiaPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float) -> bool:
        pass

class PagamentoPix(EstrategiaPagamento):
    def processar_pagamento(self, valor: float) -> bool:
        print(f"Processando R${valor:.2f} via PIX...")
        print("   -> Pagamento com PIX APROVADO.")
        return True

class PagamentoCredito(EstrategiaPagamento):
    def processar_pagamento(self, valor: float) -> bool:
        print(f"Processando R${valor:.2f} via Cartão de Crédito...")
        if valor < 1000:
            print("   -> Pagamento com Credito APROVADO.")
            return True
        else:
            print("   -> Pagamento com Credito REJEITADO (limite excedido).")
            return False

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular_frete(self, valor: float) -> float:
        pass

class FreteNormal(EstrategiaFrete):
    def calcular_frete(self, valor: float) -> float:
        custo = valor * 0.05
        print(f"Frete Normal: R${custo:.2f}")
        return custo

class FreteExpresso(EstrategiaFrete):
    def calcular_frete(self, valor: float) -> float:
        custo = valor * 0.10 + 15.00
        print(f"Frete Expresso (com taxa): R${custo:.2f}")
        return custo
