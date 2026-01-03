from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> str:
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Paid {amount} with card"


class CashPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"Paid {amount} with cash"


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount: int) -> str:
        return self.strategy.pay(amount)
