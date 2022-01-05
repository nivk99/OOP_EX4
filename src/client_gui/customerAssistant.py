from types import SimpleNamespace
from typing import List

from src.algo.algo_pokemon import AlgoPokemon
from src.client_gui.gui.guiPokemon import GuiPokemon
from src.graph import GraphInterface
from src.graph.DiGraph import DiGraph
from src.client_gui.client import Client
import json
from src.graph.geoLocation import GeoLocation
from src.pokemon_agent.agent import Agent
from src.pokemon_agent.agentInterface import AgentInterface
from src.pokemon_agent.pokemon import Pokemon
from src.pokemon_agent.pokemonInterface import PokemonInterface

PORT = 6666
HOST = '127.0.0.1'


class CustomerAssistant:
    """
    This class converts json file to objects
    """

    def __init__(self) -> None:
        self.client = Client()
        self.client.start_connection(HOST, PORT)
        self.gui_game_pokemon()

    def get_graph(self) -> GraphInterface:
        """
        :return:This method reads the graph from a json file and builds objects from it
        """
        graph_json = self.client.get_graph()
        graph = json.loads(
            graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
        graph_diGraph = DiGraph()
        for n in graph.Nodes:
            x, y, _ = n.pos.split(',')
            n.pos = SimpleNamespace(x=float(x), y=float(y))
            graph_diGraph.add_node(node_id=int(n.id), x=n.pos.x, y=n.pos.y)
        for e in graph.Edges:
            graph_diGraph.add_edge(id1=int(e.src), id2=int(e.dest), weight=float(e.w))
        return graph_diGraph

    def get_pokemon(self) -> List[PokemonInterface]:
        """
        :return:This method reads the Pokemon from the json file and builds objects from it
        """
        pokemons = json.loads(self.client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]
        pokemon_Pokemon = []
        for p in pokemons:
            x, y, _ = p.pos.split(',')
            p.pos = SimpleNamespace(x=float(x), y=float(y))
            pokemon_Pokemon.append(Pokemon(value=float(p.value), type=p.type, pos=GeoLocation(x=p.pos.x, y=p.pos.y)))
        return pokemon_Pokemon

    def add_agent(self, id: int) -> bool:
        """
        This method tells the server where to place the agents at first
        :param id: the id agent
        :return:true or false
        """
        ans: bool = self.client.add_agent("{\"id\":" + str(id) + "}")
        return ans

    def get_agents(self) -> List[AgentInterface]:
        """
        :return:This method reads the agents from a json file and builds objects from it
        """
        agents = json.loads(self.client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
        agents = [agent.Agent for agent in agents]
        agents_Agent = []
        for a in agents:
            x, y, _ = a.pos.split(',')
            a.pos = SimpleNamespace(x=float(x), y=float(y))
            agents_Agent.append(
                Agent(id=int(a.id), value=float(a.value), speed=float(a.speed), src=int(a.src), dest=int(a.dest),
                      pos=GeoLocation(x=a.pos.x, y=a.pos.y)))
        return agents_Agent

    def choose_next_edge(self, id: int, next_node: int) -> bool:
        """
        This method accepts the agent's id and tells the server where to change the agent's location
        :param id:the id agent
        :param next_node: id node
        :return:
        """

        bo = self.client.choose_next_edge("{agent_id:" + str(id) + ", next_node_id:" + str(next_node) + "}")
        return bo

    def move(self) -> None:
        """
        :return:This method tells the server to move the agents
        """
        self.client.move()

    def is_running(self) -> bool:
        """
        :return:This method tests whether it is possible to continue the game (i.e .: time is not over)
        """
        return self.client.is_running()

    def stop_connection(self) -> None:
        """
        :return:This method tells the server to stop the game
        """
        self.client.stop_connection()

    def log_in(self, id_str):
        """
        :param id_str:
        :return:This method accepts your ID as a str to connect and upload your score to the web server
        """
        self.client.log_in(id_str)

    def stop(self) -> None:
        """
        :return:This method tells the server to stop the game
        """
        self.client.stop()

    def start(self) -> None:
        """
        :return:This method starts the game
        """
        self.client.start()

    def time_to_end(self) -> float:
        """
        :return:This method brings you the end time of the game
        """
        return self.client.time_to_end()

    def gui_game_pokemon(self) -> None:
        """
        :return:This method depicts the Pokemon game with the agents
        """
        GuiPokemon(clint=self)

    def get_info(self) -> str:
        """
        :return:This method returns the details of the game to you as a string
        """
        return self.client.get_info()

    def sum_agents(self) -> int:
        """
        :return:This method returns you the number of agents
        """
        sum_agents = json.loads(self.client.get_info(), object_hook=lambda d: SimpleNamespace(**d)).GameServer
        return int(sum_agents.agents)

    def sum_pokemons(self) -> int:
        """
        :return:This method returns the number of Pokemon to you
        """
        sum_pokemons = json.loads(self.client.get_info(), object_hook=lambda d: SimpleNamespace(**d)).GameServer
        return int(sum_pokemons.pokemons)

    def sum_grade(self) -> int:
        """
        :return:This method returns you the final score
        """
        sum_grade = json.loads(self.client.get_info(), object_hook=lambda d: SimpleNamespace(**d)).GameServer
        return int(sum_grade.grade)

    def sum_moves(self) -> int:
        """
        :return:This method returns the move number to you
        """
        sum_moves = json.loads(self.client.get_info(), object_hook=lambda d: SimpleNamespace(**d)).GameServer
        return int(sum_moves.moves)

    def algo(self, graph, pokemon, agents):
        """
        :param graph:graph
        :param pokemon:list pokemon
        :param agents:list agents
        :return:This method changes the travel path of each agent according to the algorithm
        """
        AlgoPokemon(graph, pokemon, agents).algo()

    def Start_mode(self, ) -> list[int]:
        """
        :return:This method returns a list of vertex keys where the agents should be placed first
        """
        arr = AlgoPokemon(self.get_graph(), self.get_pokemon(), None).Start_mode()
        return arr

    def sleep_time(self, agents) -> float:
        """
        :param agents:
        :return:This return method balances the move number
        """
        time = AlgoPokemon(self.get_graph(), None, agents).sleep_time()
        return time
