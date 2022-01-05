from asyncio import PriorityQueue
from typing import List

from src.algo.algoPokemonInterface import AlgoPokemonInterface
from src.graph.DiGraph import DiGraph
from src.graph.GraphAlgo import GraphAlgo
from src.pokemon_agent.agentInterface import AgentInterface
from src.pokemon_agent.pokemonInterface import PokemonInterface

EPS = 0.0000000000000001


class AlgoPokemon(AlgoPokemonInterface):
    """
    This is an algorithm class suitable for any Pokemon agent
    """

    def __init__(self, graph: DiGraph, list_pokemon: List[PokemonInterface], list_agent: List[AgentInterface]):
        """
        :param graph: In the given graph
        :param list_pokemon:  A list of Pokemon that participate in the game
        :param list_agent:List of agents who participate in the game
        """
        self._graph = graph
        self._list_pokemon = list_pokemon
        self._list_agent = list_agent
        self._algo_graph = GraphAlgo(self._graph)

    def pokemon_location(self, p: PokemonInterface) -> (int, int, float):  # (src,dest,w)
        """
    This method finds the position  .:
    If there is a dot on a particular line
    The vertices of the line are A and B and the vertex you are testing is C
    Then calculate the distance between A and B.
    Then distance from A to C and distance from C to B.
    If the connection of the two distances is equal to the total distance of the point on the line, otherwise it is not on the line
    Epsilon should be kept for the number range at the end
        :param p:Pokemon
        :return:(src,dest,w)
        """
        for v in self._graph.get_all_v().values():
            p1 = v.getLocation()
            for e in self._graph.all_out_edges_of_node(v.getKey()).keys():
                p2 = self._graph.get_all_v()[e].getLocation()
                distans1 = p1.distance(p2)
                distans2 = p1.distance(p.get_pos()) + p2.distance(p.get_pos())
                if v.getLocation()== p.get_pos():
                    return v.getKey(), v.getKey(), 0
                if EPS + distans1 > distans2:
                    if v.getKey() > e and p.get_type() == -1:
                        return v.getKey(), e, self._graph.all_out_edges_of_node(v.getKey())[e]
                    if v.getKey() < e and p.get_type() == 1:
                        return e, v.getKey(), self._graph.all_out_edges_of_node(e)[v.getKey()]
        return -1, -1, float('inf')

    def agent_location(self, a: AgentInterface, p: PokemonInterface) -> (int, int, float):  # (src,dest,w)
        """
    This method finds the agent's position according to the Pokemon .:
    If there is a dot on a particular line
    The vertices of the line are A and B and the vertex you are testing is C
    Then calculate the distance between A and B.
    Then distance from A to C and distance from C to B.
    If the connection of the two distances is equal to the total distance of the point on the line, otherwise it is not on the line
    Epsilon should be kept for the number range at the end
        :param a:Agent
        :param p:Pokemon
        :return:(src,dest,w)
        """
        for v in self._graph.get_all_v().values():
            p1 = v.getLocation()
            for e in self._graph.all_out_edges_of_node(v.getKey()).keys():
                p2 = self._graph.get_all_v()[e].getLocation()
                distans1 = p1.distance(p2)
                distans2 = p1.distance(a.get_pos()) + p2.distance(a.get_pos())
                if v.getLocation() == a.get_pos():
                    return v.getKey(), v.getKey(), 0
                if EPS + distans1 > distans2:
                    if distans1 == 0 or distans2 == 0 or p1.distance(a.get_pos()) == 0 or p2.distance(a.get_pos()) == 0:
                        return -1, -1, float('inf')
                    if p.get_type() == -1:
                        return v.getKey(), e, self._graph.all_out_edges_of_node(v.getKey())[e]
                    else:
                        return e, v.getKey(), self._graph.all_out_edges_of_node(e)[v.getKey()]
        return -1, -1, float('inf')

    def algo(self) -> None:
        """
    Algorithm: Given a list of Pokemon and agents the algorithm finds for each Pokemon the best agent for it by a number of actions:
    1. Check the location of the Pokemon
    2. Check the location and agent according to the Pokemon.
    3. Check if the agent is close to the Pokemon - if so then the agent will take the Pokemon.
    4. Checks if one of the agents is available and does nothing.
    5. Check the shortest distance between agents and Pokemon - The shortest distance between agent and Pokemon will be best.
    6. Once an algorithm finds the best agent for Pokemon it adds it to the list of Pokemon that is in each agent.
    7. Finally it is sent to the tsp method which finds the agent the best way to switch between all the Pokemon.
        :return: void
        """
        self.Pokemon_priority()
        list_pokemon = self._list_pokemon
        # List of Pokemon
        for P in list_pokemon:
            poke_list = [v for p in self._list_agent for v in p.get_list_pokemon()]
            min = float('inf')
            key = None
            pokemon_location = self.pokemon_location(P)
            # List of agents
            for A in self._list_agent:
                # If Pokemon is with one of the agents
                if P in poke_list:
                    key = None
                    break
                agent_location = self.agent_location(A, P)
                # If the agent is next to Pokemon
                if agent_location[0] == pokemon_location[0] and agent_location[1] == pokemon_location[1]:
                    A.add_pokemon(P)
                    self.tsp(A)
                    key = None
                    break
                # Is the agent in a Pokemon environment?
                if agent_location[0] == pokemon_location[0]:
                    n_list = [pokemon_location[0], pokemon_location[1]]
                    for v in A.get_list_nodes():
                        n_list.append(v)
                    A.set_list_nodes(n_list)
                    if A.get_list_pokemon() is not None:
                        A.add_pokemon(P)
                    else:
                        arr = [P]
                        A.set_list_pokemon(arr)
                    if P in list_pokemon:
                        list_pokemon.remove(P)
                    self.tsp(A)
                    key = None
                    break
                short_phat = self._algo_graph.shortest_path(A.get_src(), pokemon_location[0])
                # If there is an agent without Pokemon
                if A.get_dest() == -1 and len(A.get_list_nodes()) == 0:
                    A.add_pokemon(P)
                    self.tsp(A)
                    key = None
                    break
                # Checks the shortest distance to Pokemon
                else:
                    if min > short_phat[0]:
                        min = short_phat[0]
                        key = A
            if key is not None:
                if key.get_list_pokemon() is not None:
                    key.add_pokemon(P)
                else:
                    poke = [P]
                    key.set_list_pokemon(poke)
                self.tsp(key)

    # Choose the Pokemon that is best to start with
    def Start_mode(self) -> list[int]:
        """
        Given a list of Pokemon, a method returns a list of points where agents need to start the game.
        It does this by finding the center of the points
        :return: list[Keys of vertices]
        """
        list = [self.pokemon_location(p)[0] for p in self._list_pokemon]
        list_center = []
        for i in range(len(list)):
            v = self.centerPoint(list)
            list_center.append(v)
            list.remove(v)
        return list_center

    def centerPoint(self, lis: list[int]) -> int:
        """
        This function finds the center of points according to the given list
        :param lis: list[Keys of vertices]
        :return: list[Keys of vertices]
        """
        ans = 0
        min_w = float('inf')
        for v1 in lis:
            temp = 0
            for v2 in lis:
                if temp > min_w:
                    break
                sum = self._algo_graph.shortest_path(v1, v2)[0]
                if temp < sum:
                    temp = sum
            if min_w > temp:
                min_w = temp
                ans = v1
        return ans

    # Returns priority to Pokemon
    def Pokemon_priority(self) -> None:
        """
          This method changes the list according to the highest value of the Pokemon
        :return: void
        """
        self._list_pokemon = sorted(self._list_pokemon)

    def sleep_time(self) -> float:
        """
        This function balances the readings according to the agent's speed
        :return:
        """
        max_time = max(list(self._list_agent), key=lambda n: n.get_speed()).get_speed()
        if max_time > 5:
            max_time = max_time / 100
            if max_time <= 0:
                max_time = 0
            return max_time
        else:
            return 0.1

    def tsp(self, age: AgentInterface) -> None:
        """
       This method accepts an agent and changes the route of travel to the shortest trip
        :param age:Agent
        :return:void
        """
        if age.get_list_pokemon() is None:
            return
        new = [p for p in self._list_pokemon if p in age.get_list_pokemon()]
        age.set_list_pokemon(new)
        arr = []
        for p in new:
            loc = self.pokemon_location(p)
            arr.append(loc[0])
        if len(age.get_list_nodes()) != 0:
            temp = self.__help_tsp(arr, age.get_list_nodes()[0])
            age.set_end_time(temp[1])
            arr = temp[0]
        else:
            temp = self.__help_tsp(arr, age.get_src())
            age.set_end_time(temp[1])
            arr = temp[0]
        arr.remove(arr[0])
        new = []
        if len(age.get_list_nodes()) != 0:
            new = [age.get_list_nodes()[0]]
        else:
            new = [age.get_src()]
        for v in arr:
            for p in age.get_list_pokemon():
                loc = self.pokemon_location(p)
                if loc[0] == v:
                    ph = self._algo_graph.shortest_path(new[len(new) - 1], loc[0])[1]
                    if isinstance(ph, int):
                        if ph not in new:
                            new.append(ph)
                        if loc[1] not in new:
                            new.append(loc[1])
                        break
                    for a in ph:
                        if a not in new:
                            new.append(a)
                    if loc[1] not in new:
                        new.append(loc[1])
                    break
        age.set_list_nodes(new)

    def __help_tsp(self, arr: list, src: int) -> (list, int):
        """
        This method gets a list and finds the shortest way from the source to the points that are on the list
        :param arr:List of vertices
        :param src:Starting points
        :return:List,sum
        """
        total = 0
        ans = [src]
        for v1 in arr:
            min = float('inf')
            key = -1
            for v2 in arr:
                sum = self._algo_graph.shortest_path(ans[len(ans) - 1], v2)[0]
                if min > sum:
                    min = sum
                    key = v2
            total += total + min
            ans.append(key)
            if key != v1 and len(arr) != 0 and key != -1:
                arr.remove(key)
        return ans, total
