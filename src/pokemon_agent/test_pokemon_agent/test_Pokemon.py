import unittest

from src.graph.geoLocation import GeoLocation
from src.pokemon_agent.pokemon import Pokemon
po=GeoLocation(3,5,0)
poke= Pokemon(value=5,type=1,pos=po)

po2=GeoLocation(0,0,0)
poke2= Pokemon(3,-1,po2)

class MyTestCase(unittest.TestCase):
    # Method test
    def test_get_value(self):
        self.assertEqual(5,poke.get_value())
        self.assertEqual(3, poke2.get_value())

    # Method test
    def test_get_type(self):
        self.assertEqual(1, poke.get_type())
        self.assertEqual(-1, poke2.get_type())

    # Method test
    def test_get_pos(self):
        self.assertEqual(po, poke.get_pos())
        self.assertEqual(po2, poke2.get_pos())


if __name__ == '__main__':
    unittest.main()
