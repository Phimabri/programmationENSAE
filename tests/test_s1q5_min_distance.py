import sys
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_power(1, 2, 11)[0], 11)
        self.assertEqual(g.get_path_with_power(1, 2, 10)[0], 89)



if __name__ == '__main__':
    unittest.main()
