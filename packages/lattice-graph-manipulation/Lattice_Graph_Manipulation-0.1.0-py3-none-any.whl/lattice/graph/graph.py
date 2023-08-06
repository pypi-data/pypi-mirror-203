"""
The main focal data type of the project

NOTES:
    Edges have two options - Node.successor -> next node, edge
                             Node.successor -> edge -> next node
    We choose the first one as we can avoid the extra overhead and ensure
    That edges only exist within a graph

TODO:
- Find a more elegant way to reference nodes in a graph for operations such as finding edges
"""
import uuid
from typing import Set, List, Dict

import graphviz
from ..edge.edge import Edge
from ..node.node import Node

# Prepend to node names to identify them against other attributes
NODE_ID = '_node_'


class Graph:
    # A set of exposed nodes to access when they are called for (NOTE: may not include all nodes)
    _nodes: set
    # If set to true, will display node pointers rather than labels
    # CAREFUL: may lead to attempting displaying of large data types
    _default_display_data: bool = False

    @property
    def nodes(self) -> Set[Node]:
        """Return the exposed nodes that belong to this graph """
        return self._nodes

    def __init__(self):
        self._nodes = set()  # initialise nodes as an empty set
        self.fingerprint = uuid.uuid4()

    def add_nodes(self, *hidden_nodes: Node, **nodes: Node) -> List[Node]:
        """Add nodes to a graph
        Hidden nodes are nodes that have no labels attached, they can only be accessed during the context they are
        defined in
        Normal nodes require a key value pair, and can be accessed by looking at the 'nodes' property
        To allow accessing hidden nodes, we return all added hidden nodes
        """
        added_hidden_nodes = []

        # add regular nodes
        for key, value in nodes.items():
            name = NODE_ID + key
            new_node = value.copy(key)
            setattr(self, name, new_node)
            self._nodes.add(new_node)

        # add hidden nodes
        for hidden_node in hidden_nodes:
            new_node = hidden_node.copy()
            added_hidden_nodes.append(new_node)

        return added_hidden_nodes

    def add_node(self, node: Node, label: str = None):
        """Create a node within the graph
        If no label is provided, then the node is hidden, in order to interact with hidden nodes, we return the
        created node within the context of the graph
        """
        if label:
            name = NODE_ID + label
            new_node = node.copy(label)
            setattr(self, name, new_node)
            self._nodes.add(new_node)

        else:
            new_node = node.copy()

        return new_node

    def add_edge(self, start_node: Node, end_node: Node, edge: Edge):
        """
        Add a relationship between two nodes inside the graph
        """
        start_node.add_successor(edge, end_node)
        end_node.add_predecessor(edge, start_node)

    def get_node(self, name: str):
        return getattr(self, NODE_ID + name)

    def visualise(self, display_data: bool = None):
        """
        Display nodes in the graph
        For now, this only displays visible nodes (those stored in self._nodes)
        """
        display_data = display_data or self._default_display_data
        runtime_fingerprint = uuid.uuid4()
        dot = graphviz.Digraph(str(runtime_fingerprint))
        for node in self.nodes:
            if display_data:
                origin_label = str(node.data)
            else:
                origin_label = node.get_label()
            dot.node(str(node), label=origin_label)
            for edge, next_node in node.successors:
                dot.edge(str(node), str(next_node), label=str(edge.get_data()))

        dot.render(view=True)

    # PATHFINDING

    def search_djikstra(self, start_node, end_node):
        """Perform a djikstra search between two nodes"""
        pass

    def __str__(self):
        self.visualise()
        return "​"
