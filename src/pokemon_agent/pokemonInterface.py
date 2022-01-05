from src.graph.geoLocationInterface import GeoLocationInterface


class PokemonInterface:
    """
    This interface represents the Pokemon of the Pokemon game
    """

    def get_value(self) -> float:
        """
        :return: The value of the Pokemon(The more it is the more it is worth)
        """
        raise NotImplementedError


    def get_type(self) -> int:
        """
        1 - = source> destination
        1 = Source <Destination
        :return: 1 or -1
        """
        raise NotImplementedError

    def get_pos(self) -> GeoLocationInterface:
        """
        :return: The location of Pokemon
        """
        raise NotImplementedError

