from src.graph import GraphAlgoInterface
from src.pokemon_agent.agentInterface import AgentInterface
from src.pokemon_agent.pokemonInterface import PokemonInterface


class Agent(AgentInterface):
    """
This class describes the agents
    """

    def __init__(self, id: int = 0, value: float = 0, src: int = 0, dest: int = 0,
                 pos: GraphAlgoInterface = None, speed: float = 0, ) -> None:
        """
        constructor
        :param id: Agent number
        :param value:Grade
        :param src:source
        :param dest:target
        :param pos:Location
        :param speed:speed
        """
        self._id = id
        self._value = value
        self._src = src
        self._dest = dest
        self._speed = speed
        self._pos = pos
        self._list_pokemon = []
        self._list_nodes = []
        self._remove = self._src
        self._end_time = 0.0

    def add_pokemon(self, poke) -> None:
        """
        :param poke:
        :return:Adds to the list of Pokemon
        """
        self._list_pokemon.append(poke)

    def get_end_time(self) -> float:
        """
        :return: The end of time
        """
        return self._end_time

    def set_end_time(self, time: float) -> None:
        """
        :param time:
        :return:Change the end of time
        """
        self._end_time = time

    def get_list_nodes(self) -> list[int]:
        """
        :return:List of vertices
        """
        return self._list_nodes

    def set_list_nodes(self, nodes: list[int]) -> None:
        """
         Changes the list of vertex keys
        :param nodes:
        :return:
        """
        self._list_nodes = nodes

    def get_list_pokemon(self) -> list[PokemonInterface]:
        """
        :return:List of Pokemon
        """
        return self._list_pokemon

    def set_list_pokemon(self, poke: list[PokemonInterface]) -> None:
        """
        Change list
        :param poke:
        :return:
        """
        self._list_pokemon = poke

    def next_node(self) -> int:
        """
        :return:The next organ on the list
        """
        if len(self._list_nodes) == 0:
            self._remove = self._src
            return self._src
        else:
            next = self._list_nodes[0]
            self._remove = next
            self._list_nodes.remove(next)
            return next

    def ged_id(self) -> int:
        """
        :return:The agent's number
        """
        return self._id

    def get_value(self) -> float:
        """
        :return:Grade
        """
        return self._value

    def get_src(self) -> int:
        """
        :return:source
        """
        return self._src

    def get_dest(self) -> int:
        """
        :return:target
        """
        return self._dest

    def get_speed(self) -> float:
        """
        :return:speed
        """
        return self._speed

    def get_pos(self) -> GraphAlgoInterface:
        """
        :return:Location
        """
        return self._pos

    def get_remove_node(self):
        """
        :return:remove_node
        """
        return self._remove

    def __str__(self):
        """
        :return:A string of the class
        """
        return f"id:{self._id},  value:{self._value}, src:{self._src}, dest:{self._dest}, speed:{self._speed}, pos:{self._pos}"

    def __repr__(self) -> str:
        """
        :return:A string of the class
        """
        return f"id:{self._id},  value:{self._value}, src:{self._src}, dest:{self._dest}, speed:{self._speed}, pos:{self._pos}"
