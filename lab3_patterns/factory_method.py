from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    def deliver(self) -> str:
        return "Deliver by road"


class Ship(Transport):
    def deliver(self) -> str:
        return "Deliver by sea"


class Logistics(ABC):
    def plan_delivery(self) -> str:
        transport = self.create_transport()
        return transport.deliver()

    @abstractmethod
    def create_transport(self) -> Transport:
        pass


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
