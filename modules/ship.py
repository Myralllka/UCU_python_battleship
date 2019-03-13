import modules.chars as chars


class Ship:
    """
    class for representing ship in the game
    """

    def __init__(self,
                 bow: tuple,
                 horizontal: bool):
        """
        initialization of the class
        :param bow: coordinates of ships bow
        :param horizontal: orientation of the ship: True if horizontal,
        False if vertical
        char - char for drawing the ship
        char_hit - char for drawing the hit ship
        __length - tuple, privet attribute to representation of the ship length
        __hit - list, privet attribute to representation of the ship in the
        "hit or not" way
        """
        self.bow = bow
        self.horizontal = horizontal
        self.__length = (0, 0)
        self.__hit = [True]
        self.char = chars.SHIP_AREA
        self.char_hit = chars.HURT_AREA

    @property
    def hit(self):
        return self.__hit

    @hit.setter
    def hit(self, val):
        self.__hit = val

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        self.__length = val

    def __str__(self):
        """
        representing ship in string function
        :return: description of the Ship
        """
        return 'Ship with bow on {} and {} length'.format(self.bow,
                                                          self.length)

    def __repr__(self):
        """
        representing player in repr function
        :return: type of the ship
        """
        return str(type(self))

    def get_char(self, coordinate: tuple) -> str:
        """
        Method to get char of the ship in current coordinates (is it hit or
        not)
        :param coordinate: coordinate of needed unit
        :return: needed char
        """
        if isinstance(self, EmptyDeck) or isinstance(self, WarningDeck):
            return self.char
        tmp1 = abs(self.bow[0] - coordinate[0])
        tmp2 = abs(self.bow[1] - coordinate[1])
        flag = (tmp1 < self.length[0] and
                tmp2 < self.length[1])
        if flag and self.hit[max(tmp1, tmp2)]:
            return self.char_hit
        else:
            return self.char

    def shoot_at(self, coordinate: tuple) -> tuple:
        """
        Method to shoot at the ship
        :param coordinate: coordinate of needed unit
        :return: tuple of booleans. first element mean that you hurt the
        ship or miss, and the second mean that you destroy the ship at all
        or not
        """
        if isinstance(self, EmptyDeck) or isinstance(self, WarningDeck):
            self.char = chars.MISSED_AREA
            return tuple([False, False])
        tmp1 = abs(self.bow[0] - coordinate[0])
        tmp2 = abs(self.bow[1] - coordinate[1])
        flag = (tmp1 < self.length[0] and
                tmp2 < self.length[1])
        if flag:
            self.hit[max(tmp1, tmp2)] = True
            if all(self.hit):
                return tuple([True, True])
            else:
                return tuple([True, False])
        return tuple([False, False])


class EmptyDeck(Ship):
    """
    class for representing empty deck in the game
    """

    def __init__(self, bow: tuple):
        """
        initialization of the empty deck element
        :param bow: coordinates of ships bow
        length - tuple
        """
        super().__init__(bow, True)
        self.length = (1, 1)
        self.char = chars.EMPTY_AREA


class WarningDeck(Ship):
    """
    class for representing warning deck (looks like empty deck, but you
    cannot situated ships there)
    """
    def __init__(self, bow: tuple):
        """
        initialization of the empty deck element
        length - tuple
        """
        super().__init__(bow, True)
        self.length = (1, 1)
        self.char = chars.EMPTY_AREA


class OneDeck(Ship):
    """
    class for representation one deck ship
    """
    def __init__(self, bow: tuple):
        """
        initialization of the one deck ship
        """
        super().__init__(bow, True)
        self.hit = [False]
        self.length = (1, 1)


class TwoDeck(Ship):
    """
    class for representation two deck ship
    """
    def __init__(self, bow: tuple, horizontal: bool):
        """
        initialization of the two deck ship
        """
        super().__init__(bow, horizontal)
        self.hit = [False for i in range(2)]
        self.length = (1, 2) if horizontal else (2, 1)


class ThreeDeck(Ship):
    """
    class for representation three deck ship
    """
    def __init__(self, bow: tuple, horizontal: bool):
        """
        initialization of the three deck ship
        """
        super().__init__(bow, horizontal)
        self.hit = [False for i in range(3)]
        self.length = (1, 3) if horizontal else (3, 1)


class FourDeck(Ship):
    """
    class for representation four deck ship
    """
    def __init__(self, bow: tuple, horizontal: bool):
        """
        initialization of the four deck ship
        """
        super().__init__(bow, horizontal)
        self.hit = [False for i in range(4)]
        self.length = (1, 4) if horizontal else (4, 1)
