class GeoLocationInterface:
    """
 This interface represents a geo location <x,y,z>, (aka Point3D data).
    """

    def get_x(self) -> float:
        """
        :return: x
        """
        raise NotImplementedError

    def get_y(self) -> float:
        """
        :return: y
        """
        raise NotImplementedError

    def get_z(self) -> float:
        """
        :return: z
        """
        raise NotImplementedError

    def distance(self, g) -> float:
        """
        :param g: The second point for calculating the distance
        :return: Distance between 2 vertices with 3 values
        """
        raise NotImplementedError
