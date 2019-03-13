class Game:
    """
    Class for the game
    """
    def __init__(self, fields: list, players: list):
        """
        initialization of Game class
        :param fields: list of fields
        :param players: list of players
        """
        self.__fields = fields
        self.__players = players
        self.__current_player = 0

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, val):
        self.__fields = val

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, val):
        self.__players = val

    @property
    def current_player(self):
        return self.__current_player

    @current_player.setter
    def current_player(self, val):
        self.__current_player = val

    def read_position(self):
        """
        read coordinates where player wants to shoot
        :return: coordinates where to shoot
        """
        return self.players[self.current_player].read_position()

    def field_without_ships(self):
        """
        Method to print field without all ships viewed
        :return :string, needed field
        """
        return self.fields[self.current_player].field_without_ships()

    def field_with_ships(self):
        """
        Method to print field with all ships viewed
        :return :string, needed field
        """
        return self.fields[self.current_player].field_with_ships()

    def is_end(self) -> bool:
        """
        Method to check if it is the end of the game or not
        :return: True if somebody win, False if not
        """
        result1 = []
        result2 = []
        for i in range(10):
            for j in range(10):
                result1.extend(self.fields[self.current_player]
                               .ships[i][j].hit)
        for i in range(10):
            for j in range(10):
                result2.extend(self.fields[-1 * self.current_player + 1]
                               .ships[i][j].hit)
        if all(result1) or all(result2):
            return True
        return False
