from abc import ABC, abstractmethod
from rosetta.ir.nodes import RosettaNode

class CipherBackend(ABC):
    @property
    @abstractmethod
    def language_id(self) -> str:
        pass

    @property
    @abstractmethod
    def style_guide(self) -> str:
        pass

    @abstractmethod
    def emit(self, node: RosettaNode) -> str:
        pass
