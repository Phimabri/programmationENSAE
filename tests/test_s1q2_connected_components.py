# This will work if ran from the root folder.
import sys
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_GraphCC(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file("input/network.00.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})})

    def test_network01(self):
        g = graph_from_file("input/network.01.in")
        cc = g.connected_components_set()
        self.assertEqual(cc, {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})})

    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        cc = g.connected_components_set()
        self.assertIn(frozenset({1,2,3,4}),cc)

    def test_network03(self):
        g = graph_from_file("input/network.03.in")
        cc = g.connected_components_set()
        self.assertIn(frozenset({1,2,3,4}),cc)

if __name__ == '__main__':
    unittest.main()
