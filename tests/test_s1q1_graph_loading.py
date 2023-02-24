# This will work if ran from the root folder.
import sys
sys.path.append("delivery_network/")

import unittest
from graph import Graph, graph_from_file

class Test_GraphLoading(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 9)

    def test_network01(self):
        g = graph_from_file("input/network.01.in")
        self.assertEqual(g.nb_nodes, 7)
        self.assertEqual(g.nb_edges, 5)

    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)
        self.assertIn([3,4,3],g.graph[2])
        self.assertIn([4,4,2],g.graph[3])
        self.assertIn([4,11,6],g.graph[1])

    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.nb_nodes, 10)
        self.assertEqual(g.nb_edges, 4)

if __name__ == '__main__':
    unittest.main()
