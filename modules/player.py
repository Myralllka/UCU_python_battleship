class Player:
    """
    class for representing Player of the game
    """
    def __init__(self, name: str):
        """
        initialization of class
        :param name: player name
        """
        self.__name = name

    def __str__(self):
        """
        representing player in string function
        :return: name of the player
        """
        return self.__name

    def __repr__(self):
        """
        representing player in repr function
        :return: self name
        """
        return self.__name

    @property
    def name(self):
        return self.__name

    @staticmethod
    def converter_to_normal_coordinates(coordinates: tuple) -> tuple:
        """
        function to convert inputted coordinates in normal format
        :param coordinates: inputted coordinates
        :return: normal format of inputted coordinates
        """
        columns = list('ABCDEFGHIJ')
        assert coordinates[0] in columns, 'incorrect input'
        assert int(coordinates[1]) in range(1, 11), 'incorrect input'
        # print(coordinates[1])
        i = int(coordinates[1]) - 1
        j = columns.index(coordinates[0])
        return tuple([i, j])

    def read_position(self):
        """
        read coordinates where player wants to shoot
        :return: coordinates where to shoot
        """
        tmp = input('{} > '.format(self.name))
        tmp = tuple([tmp[:1], tmp[1:]])
        return Player.converter_to_normal_coordinates(tmp)
