import unittest

from src.graph.GraphAlgo import GraphAlgo
from src.graph.DiGraph import DiGraph

graph = DiGraph()

# add the nodes

# key -> 0
graph.add_node(0, 0, 0)
# key -> 1
graph.add_node(1, 0, 0)
# key -> 2
graph.add_node(2, 0, 0)
# key -> 3
graph.add_node(3, 0, 0)
# key -> 4
graph.add_node(4, 0, 0)

# add the edge

# key -> 0
graph.add_edge(0, 1, 2)
graph.add_edge(0, 4, 3)

# key -> 1
graph.add_edge(1, 0, 3)
graph.add_edge(1, 3, 1)

# key -> 2
graph.add_edge(2, 3, 2)
graph.add_edge(2, 4, 2)

# key -> 3
graph.add_edge(3, 1, 5)
graph.add_edge(3, 2, 4)

# key -> 4
graph.add_edge(4, 0, 5)
graph.add_edge(4, 2, 1)

graph_algo = GraphAlgo(graph)


class MyTestCase(unittest.TestCase):
    # This is a method of testing
    def test_get_graph(self):
        self.assertEqual(graph, graph_algo.get_graph())

    # This is a method of testing
    def test_shortest_path(self):
        self.assertEqual(3, graph_algo.shortest_path(0, 3)[0])

    # This is a method of testing
    def test_TSP(self):
        arr = [0, 1, 4]
        tsp = graph_algo.TSP(arr)[0]
        tsp_sum = graph_algo.TSP(arr)[1]
        self.assertEqual(6, tsp_sum)
        self.assertEqual(1, tsp[0])
        self.assertEqual(0, tsp[1])
        self.assertEqual(4, tsp[2])


if __name__ == '__main__':
    unittest.main()
