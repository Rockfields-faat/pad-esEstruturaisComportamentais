from abc import ABC, abstractmethod

class CalculoValor(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass

class ValorBase(CalculoValor):
    def __init__(self, valor: float):
        self._valor = valor

    def calcular(self) -> float:
        return self._valor

class DecoradorCalculo(CalculoValor):
    def __init__(self, componente: CalculoValor):
        self._componente = componente

    @abstractmethod
    def calcular(self) -> float:
        pass

class DescontoPix(DecoradorCalculo):
    def calcular(self) -> float:
        valor = self._componente.calcular()
        desconto = valor * 0.05
        print(f"Aplicando 5% de desconto PIX: -R${desconto:.2f}")
        return valor - desconto

class TaxaEmbalagemPresente(DecoradorCalculo):
    def calcular(self) -> float:
        valor = self._componente.calcular()
        taxa = 5.00
        print(f"Adicionando taxa de embalagem presente: +R${taxa:.2f}")
        return valor + taxa
