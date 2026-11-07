from abc import ABC, abstractmethod
from typing import List
from rosetta.ir.nodes import RosettaNode, Program

class HermesPass(ABC):
    @abstractmethod
    def transform(self, node: RosettaNode) -> RosettaNode:
        pass

class HermesPipeline:
    def __init__(self, passes: List[HermesPass] = None):
        self.passes = passes or []

    def add_pass(self, h_pass: HermesPass):
        self.passes.append(h_pass)

    def run(self, node: RosettaNode) -> RosettaNode:
        current_node = node
        for h_pass in self.passes:
            current_node = h_pass.transform(current_node)
        return current_node
