import unittest

from src.graph.geoLocation import GeoLocation

g1=GeoLocation(1,2,3)
g2=GeoLocation(2,5,3)


class MyTestCase(unittest.TestCase):
    # This is a method of testing
    def test_get_x(self):
        self.assertEqual(1,g1.get_x())
        self.assertEqual(2, g2.get_x())

    # This is a method of testing
    def test_get_y(self):
        self.assertEqual(2, g1.get_y())
        self.assertEqual(5, g2.get_y())

    # This is a method of testing
    def test_get_z(self):
        self.assertEqual(3, g1.get_z())
        self.assertEqual(3, g2.get_z())

    # This is a method of testing
    def test_distance(self):
        self.assertEqual(3,int(g1.distance(g2)))


if __name__ == '__main__':
    unittest.main()
