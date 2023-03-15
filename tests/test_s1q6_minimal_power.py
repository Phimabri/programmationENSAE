# This will work if ran from the root folder.
import sys
sys.path.append("delivery_network")

from graph import graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.min_power(1, 4)[0], 11)
        self.assertEqual(g.min_power(2, 4)[0], 10)


    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        self.assertEqual(g.min_power(1, 3)[0], 4)
        self.assertEqual(g.min_power(1, 2)[0], 4)

    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.min_power(1, 4)[0], 4)
        self.assertEqual(g.min_power(1, 6)[1], None)

if __name__ == '__main__':
    unittest.main()
