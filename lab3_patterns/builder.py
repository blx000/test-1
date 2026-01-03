from dataclasses import dataclass


@dataclass
class Computer:
    cpu: str
    ram_gb: int
    ssd_gb: int
    gpu: str | None = None


class ComputerBuilder:
    def __init__(self):
        self._cpu = "Base CPU"
        self._ram_gb = 8
        self._ssd_gb = 256
        self._gpu = None

    def cpu(self, name: str):
        self._cpu = name
        return self

    def ram(self, gb: int):
        self._ram_gb = gb
        return self

    def ssd(self, gb: int):
        self._ssd_gb = gb
        return self

    def gpu(self, name: str):
        self._gpu = name
        return self

    def build(self) -> Computer:
        return Computer(
            cpu=self._cpu,
            ram_gb=self._ram_gb,
            ssd_gb=self._ssd_gb,
            gpu=self._gpu
        )
