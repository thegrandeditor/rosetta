from abc import ABC, abstractmethod
from rosetta.ir.nodes import RosettaNode

class BabelFrontend(ABC):
    @property
    @abstractmethod
    def language_id(self) -> str:
        pass

    @property
    @abstractmethod
    def supported_version(self) -> str:
        pass

    @abstractmethod
    def parse(self, source: str) -> RosettaNode:
        pass
