"""
This file serves as an example of building graphs within the capabilities of the code we have
"""
from lattice import Node
from lattice import TraverseEdge as CEdge
from lattice import BBTree, Graph

# Random bullshit
graph1 = Graph()

mynode = Node([1, 2, 3])
a = Node(2)

graph1.add_nodes(mynode=mynode)
graph1.add_nodes(a=a)
graph1.add_nodes(b=Node(3))
graph1.add_nodes(c=Node(4))

graph1.add_edge(graph1.get_node('mynode'), graph1.get_node('a'), CEdge(5, "drive"))
graph1.add_edge(graph1.get_node('a'), graph1.get_node('b'), CEdge(5, "drive"))
graph1.add_edge(graph1.get_node('b'), graph1.get_node('c'), CEdge(5, "drive"))

mynode.pointer.append(4)


# Balanced Binary Tree
def build_binary_tree(n):
    graph = BBTree(Node(0))
    for i in range(1, n + 1):
        graph.add_node(Node(i))

    return graph


graph2 = build_binary_tree(20)

if __name__ == "__main__":
    # We have created several graphs, uncomment lines here to visualise them
    # graph1.visualise()
    # graph2.visualise()
    # print(graph1)
    # print(graph2)


    pass
