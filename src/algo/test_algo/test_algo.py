import unittest

from src.algo.algo_pokemon import AlgoPokemon
from src.pokemon_agent.pokemon import Pokemon
from src.graph.geoLocation import GeoLocation
from src.pokemon_agent.agent import Agent
from src.graph.DiGraph import DiGraph

graph = DiGraph()

# add the nodes

# key -> 0
graph.add_node(0, 0, 0)
# key -> 1
graph.add_node(1, 3, 3)
# key -> 2
graph.add_node(2, 6, 6)
# key -> 3
graph.add_node(3, 6, 2)
# key -> 4
graph.add_node(4, 2, 7)

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

# list agents:
list_agent = []
po1 = GeoLocation(0, 0, 0)
ag1 = Agent(id=0, value=0, src=0, dest=-1, pos=po1, speed=1.0)
list_agent.append(ag1)

po2 = GeoLocation(6, 6, 0)
ag2 = Agent(id=0, value=0, src=0, dest=-1, pos=po2, speed=1.0)
list_agent.append(ag2)

# list pokemon:
list_pokemon = []

po11 = GeoLocation(2, 7, 0)
poke1 = Pokemon(value=5, type=1, pos=po11)
list_pokemon.append(poke1)

po22 = GeoLocation(6, 2, 0)
poke2 = Pokemon(value=10, type=1, pos=po22)
list_pokemon.append(poke2)

po33 = GeoLocation(3, 3, 0)
poke3 = Pokemon(value=12, type=1, pos=po33)
list_pokemon.append(poke3)

po44 = GeoLocation(0, 0, 0)
poke4 = Pokemon(value=1, type=1, pos=po44)
list_pokemon.append(poke4)

algo = AlgoPokemon(graph=graph, list_pokemon=list_pokemon, list_agent=list_agent)


class MyTestCase(unittest.TestCase):
    # Method test
    def test_pokemon_location(self):
        self.assertEqual(4, algo.pokemon_location(poke1)[0])
        self.assertEqual(4, algo.pokemon_location(poke1)[1])

        self.assertEqual(3, algo.pokemon_location(poke2)[0])
        self.assertEqual(3, algo.pokemon_location(poke2)[1])

        self.assertEqual(1, algo.pokemon_location(poke3)[0])
        self.assertEqual(1, algo.pokemon_location(poke3)[1])

        self.assertEqual(0, algo.pokemon_location(poke4)[0])
        self.assertEqual(0, algo.pokemon_location(poke4)[1])

    # Method test
    def test_agent_location(self):
        self.assertEqual(0, algo.agent_location(ag1, poke1)[0])
        self.assertEqual(2, algo.agent_location(ag2, poke2)[0])

    # Method test
    def test_algo(self):
        ag1.add_pokemon(poke1)
        ag2.add_pokemon(poke2)
        algo.algo()
        self.assertEqual(poke3, ag1.get_list_pokemon()[0])
        self.assertEqual(poke2, ag2.get_list_pokemon()[0])
        self.assertEqual(poke1, ag1.get_list_pokemon()[1])
        self.assertEqual(poke4, ag1.get_list_pokemon()[2])

    # Method test
    def test_Start_mode(self):
        arr = algo.Start_mode()
        print(arr)
        self.assertEqual(0, arr[0])
        self.assertEqual(1, arr[1])
        self.assertEqual(4, arr[2])
        self.assertEqual(3, arr[3])

    # Method test
    def test_centerPoint(self):
        p = algo.centerPoint([1, 4, 3, 0])
        self.assertEqual(0, p)

    # Method test
    def test_Pokemon_priority(self):
        algo.Pokemon_priority()
        self.assertEqual(poke3, algo._list_pokemon[0])
        self.assertEqual(poke2, algo._list_pokemon[1])
        self.assertEqual(poke1, algo._list_pokemon[2])
        self.assertEqual(poke4, algo._list_pokemon[3])

    # Method test
    def test_tsp(self):
        ag1.add_pokemon(poke4)
        ag1.add_pokemon(poke3)
        ag1.add_pokemon(poke2)
        ag1.add_pokemon(poke1)
        algo.tsp(ag1)
        self.assertEqual(poke3, ag1.get_list_pokemon()[0])
        self.assertEqual(poke2, ag1.get_list_pokemon()[1])
        self.assertEqual(poke1, ag1.get_list_pokemon()[2])
        self.assertEqual(poke4, ag1.get_list_pokemon()[3])


if __name__ == '__main__':
    unittest.main()
