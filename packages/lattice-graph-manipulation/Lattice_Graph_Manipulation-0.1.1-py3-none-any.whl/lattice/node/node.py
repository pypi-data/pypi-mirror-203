"""
Basic Node
"""
from __future__ import annotations

from lattice.edge.edge import Edge


class Node:
    _successors: set
    _predecessors: set
    _label: str

    def __init__(self, pointer, label=None):
        self.pointer = pointer
        self._predecessors = set()
        self._successors = set()
        self._label = label

    def copy(self, label=None):
        return Node(self.pointer, label)

    @property
    def data(self):
        return self.pointer

    @property
    def successors(self):
        return self._successors

    @property
    def predecessors(self):
        return self._predecessors

    def add_successor(self, edge: Edge, node: Node):
        self._successors.add((edge, node))

    def add_predecessor(self, edge: Edge, node: Node):
        self._predecessors.add((edge, node))

    def get_label(self):
        return self._label
