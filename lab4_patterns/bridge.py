from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass


class TV(Device):
    def is_enabled(self) -> bool:
        return True


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def check(self):
        return self.device.is_enabled()
