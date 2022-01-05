import unittest

from src.pokemon_agent.pokemon import Pokemon
from src.graph.geoLocation import GeoLocation
from src.pokemon_agent.agent import Agent

po1 = GeoLocation(3, 5, 0)
ag1 = Agent(id=0, value=5, src=0, dest=1, pos=po1, speed=1.0)
l1 = [0, 1, 2, 3]
ag1.set_list_nodes(l1)

po2 = GeoLocation(3, 5, 0)
ag2 = Agent(1, 3, 1, 0, po2, 2.0)
l2 = [3, 2, 1, 0]
ag2.set_list_nodes(l2)


class MyTestCase(unittest.TestCase):

    # Method test
    def test_add_pokemon(self):
        po1 = GeoLocation(3, 5, 0)
        poke1 = Pokemon(5, 1, po1)
        ag1.add_pokemon(poke1)

        po2 = GeoLocation(0, 0, 0)
        poke2 = Pokemon(3, -1, po2)
        ag2.add_pokemon(poke2)

        if poke1 not in ag1.get_list_pokemon():
            self.fail("faile add pokemon1")
        if poke2 not in ag2.get_list_pokemon():
            self.fail("faile add pokemon2")

    # Method test
    def test_get_end_time(self):
        ag1.set_end_time(1)
        ag2.set_end_time(2)
        self.assertEqual(1, ag1.get_end_time())
        self.assertEqual(2, ag2.get_end_time())

    # Method test
    def test_set_end_time(self):
        ag1.set_end_time(3)
        ag2.set_end_time(5)
        self.assertEqual(3, ag1.get_end_time())
        self.assertEqual(5, ag2.get_end_time())

    # Method test
    def test_get_list_nodes(self):
        self.assertEqual(l1, ag1.get_list_nodes())
        self.assertEqual(l2, ag2.get_list_nodes())

    # Method test
    def test_set_list_nodes(self):
        l1 = [0, 1, 0, 1]
        ag1.set_list_nodes(l1)
        l2 = [1, 1, 1, 0]
        ag2.set_list_nodes(l2)
        self.assertEqual(l1, ag1.get_list_nodes())
        self.assertEqual(l2, ag2.get_list_nodes())

    # Method test
    def test_get_list_pokemon(self):
        po1 = GeoLocation(3, 5, 0)
        poke1 = Pokemon(5, 1, po1)
        po2 = GeoLocation(3, 5, 0)
        poke2 = Pokemon(5, 1, po2)
        li = []
        li.append(poke1)
        li.append(poke2)
        ag1.set_list_pokemon(li)
        self.assertEqual(li, ag1.get_list_pokemon())

    # Method test
    def test_set_list_pokemon(self):
        po1 = GeoLocation(3, 5, 0)
        poke1 = Pokemon(5, 1, po1)
        po2 = GeoLocation(3, 5, 0)
        poke2 = Pokemon(5, 1, po2)
        li = []
        li.append(poke1)
        li.append(poke2)
        ag1.set_list_pokemon(li)
        self.assertEqual(li, ag1.get_list_pokemon())

    # Method test
    def test_next_node(self):
        l1 = [0, 1, 2, 3]
        ag1.set_list_nodes(l1)
        l2 = [3, 2, 1, 0]
        ag2.set_list_nodes(l2)
        self.assertEqual(0, ag1.next_node())
        self.assertEqual(3, ag2.next_node())

    # Method test
    def test_ged_id(self):
        self.assertEqual(0, ag1.ged_id())
        self.assertEqual(1, ag2.ged_id())

    # Method test
    def test_get_value(self):
        self.assertEqual(5, ag1.get_value())
        self.assertEqual(3, ag2.get_value())

    # Method test
    def test_get_src(self):
        self.assertEqual(0, ag1.get_src())
        self.assertEqual(1, ag2.get_src())

    # Method test
    def test_get_dest(self):
        self.assertEqual(1, ag1.get_dest())
        self.assertEqual(0, ag2.get_dest())

    # Method test
    def test_get_speed(self):
        self.assertEqual(1.0, ag1.get_speed())
        self.assertEqual(2.0, ag2.get_speed())

    # Method test
    def test_get_pos(self):
        self.assertEqual(po1, ag1.get_pos())
        self.assertEqual(po2, ag2.get_pos())

    # Method test
    def test_get_remove_node(self):
        v1 = ag1.next_node()
        v2 = ag2.next_node()
        self.assertEqual(v1, ag1.get_remove_node())
        self.assertEqual(v2, ag2.get_remove_node())


if __name__ == '__main__':
    unittest.main()
