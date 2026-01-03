from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next = next_handler

    @abstractmethod
    def handle(self, amount: int):
        pass


class Manager(Handler):
    def handle(self, amount: int):
        if amount <= 1000:
            return "Approved by Manager"
        return self.next.handle(amount)


class Director(Handler):
    def handle(self, amount: int):
        if amount <= 5000:
            return "Approved by Director"
        return "Request denied"
