from src.graph import GraphAlgoInterface
from src.pokemon_agent.pokemonInterface import PokemonInterface


class AgentInterface:
    """
    This Interface represents the agent of the Pokemon game
    """

    def ged_id(self) -> int:
        """
        :return: The agent's number
        """
        raise NotImplementedError

    def get_value(self) -> float:
        """
        :return: As much as he caught Pokemon
        """
        raise NotImplementedError

    def get_src(self) -> int:
        """
        :return: The source of the agent
        """
        raise NotImplementedError

    def get_dest(self) -> int:
        """
        :return: Where the agent wants to go
        """
        raise NotImplementedError

    def get_speed(self) -> float:
        """
        :return: Agent speed per second
        """
        raise NotImplementedError

    def get_pos(self) -> GraphAlgoInterface:
        """
        :return:The agent's local location
        """
        raise NotImplementedError

    def get_end_time(self) -> float:
        """
        :return: Returns when the agent finishes
        """
        raise NotImplementedError

    def set_end_time(self, time: float) -> None:
        """
        :param time:
        :return:Changes the end time
        """
        raise NotImplementedError

    def get_list_nodes(self) -> list[int]:
        """
        :return: a list of vertex keys
        """
        raise NotImplementedError

    def set_list_nodes(self, nodes: list[int]) -> None:
        """
        Changes the list of vertex keys
        :param nodes: a list of vertex keys
        :return: void
        """
        raise NotImplementedError

    def get_list_pokemon(self) -> list[PokemonInterface]:
        """
        :return: a list of Pokemon
        """
        raise NotImplementedError

    def set_list_pokemon(self, poke: list[PokemonInterface]) -> None:
        """
        Changes the list of Pokemon
        :param poke:list of Pokemon
        :return:void
        """
        raise NotImplementedError

    def next_node(self) -> int:
        """
        :return: The next vertex in the list
        """
        raise NotImplementedError

    def add_pokemon(self, poke) -> None:
        """
        :param poke:Pokemon
        :return: Adds to the list of Pokemon
        """
        raise NotImplementedError









