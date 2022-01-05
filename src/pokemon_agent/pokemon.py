from src.graph.geoLocationInterface import GeoLocationInterface
from src.pokemon_agent.pokemonInterface import PokemonInterface


class Pokemon(PokemonInterface):
    """
 This class describes the Pokemon
    """

    def __init__(self, value: float = 0, type: int = 1, pos: GeoLocationInterface = None) -> None:
        """
        constructor
        :param value:How much is it worth?
        :param type:Is on a edge rising or falling
        :param pos:Location
        """
        self._value = value
        self._type = type
        self._pos = pos

    def get_value(self) -> float:
        """
        :return:How much is it worth?
        """
        return self._value

    def get_type(self) -> int:
        """
        :return:Is on a edge rising or falling
        """
        return self._type

    def get_pos(self) -> GeoLocationInterface:
        """
        :return:Location
        """
        return self._pos

    def __eq__(self, other) -> int:
        return self._pos==other.get_pos() and self._value == other.get_value() and self._type == other.get_type()

    def __lt__(self, other: PokemonInterface) -> int:
        """
       Sorts a list from largest to smallest according to the value of Pokemon
        :param other:Pokemon
        :return:Who is bigger
        """
        return self._value > other.get_value()

    def __repr__(self) -> str:
        """
        :return:A string of the class
        """
        return f"value: {self._value}, type:{self._type}, pos:{self._pos}"
