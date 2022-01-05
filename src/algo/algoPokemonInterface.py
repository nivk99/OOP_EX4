from src.pokemon_agent.agentInterface import AgentInterface
from src.pokemon_agent.pokemonInterface import PokemonInterface


class AlgoPokemonInterface:
    """
    This class describes the algorithm interface
    """

    def pokemon_location(self, p: PokemonInterface) -> (int, int, float):
        """
        This method should find the location of the Pokemon
        :param p:Pokemon
        :return: (src,dest,w)
        """
        raise NotImplementedError

    def agent_location(self, a: AgentInterface, p: PokemonInterface) -> (int, int, float):
        """
        This method should find the location of the Agent
        :param a:Agent
        :param p::Pokemon
        :return:(src,dest,w)
        """
        raise NotImplementedError

    def algo(self) -> None:
        """
        This method makes decisions about which agent the Pokemon is associated with
        :return: void
        """
        raise NotImplementedError

    def Start_mode(self) -> list[int]:
        """
        This method selects each agent where to start the game
        :return: List of keys of vertices
        """
        raise NotImplementedError

    def centerPoint(self, lis: list[int]) -> int:
        """
        This method finds the center from the list
        :param lis: List of keys of vertices
        :return: The apex of the center
        """

        raise NotImplementedError

    def Pokemon_priority(self) -> None:
        """
        This method changes the list of Pokemon based on their highest value
        :return: void
        """
        raise NotImplementedError

    def sleep_time(self) -> float:
        """
        This method balances the readings according to the agent's speed
        :return: void
        """
        raise NotImplementedError

    def tsp(self, age: AgentInterface) -> None:
        """
        This method finds the shortest way out of a list of Pokemon that are in the agent
        :param age:Agent
        :return: void
        """
        raise NotImplementedError
