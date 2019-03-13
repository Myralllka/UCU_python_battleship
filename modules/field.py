from modules.ship import *
import modules.chars as chars


class Field:
    """
    class for representation playing field - array of different kinds of the ships
    """
    def __init__(self, ships: list):
        """
        initialization of the class
        :param ships: array of Ship instances
        """
        self.__ships = ships

    @property
    def ships(self):
        return self.__ships

    @ships.setter
    def ships(self, val):
        self.__ships = val

    def __str__(self):
        """
        representing field in string function
        :return: function for printing field
        """
        return self.field_without_ships()

    def __repr__(self):
        """
        representing player in repr function
        :return: information that it is an field
        """
        return "Field with ships"

    def shoot_at(self, coordinates: tuple) -> bool:
        """
        Method to shoot at the ship. if shoot in the ship and destroy it -
        shoot at all Warning ships around this
        :param coordinates: coordinate of needed unit
        :return: True if hurt the ship, false if not
        """
        x = coordinates[0]
        y = coordinates[1]
        ship = self.ships[x][y]
        tmp_tuple = ship.shoot_at(coordinates)
        if tmp_tuple[1]:
            for i in range(ship.bow[0] - 1, ship.bow[0] + ship.length[0] + 1):
                for j in range(ship.bow[1] - 1,
                               ship.bow[1] + ship.length[1] + 1):
                    if i in range(0, 10) and j in range(0, 10):
                        self.ships[i][j].shoot_at((i, j))
        return tmp_tuple[0]

    def field_without_ships(self) -> str:
        """
        Method to print field without all ships viewed
        :return :string, needed field
        """
        new_line = ''
        i, j = 0, 0
        line = 'ABCDEFGHIJ'
        new_line += '\n    | ' + ' | '.join(line) + ' |'
        for row in self.ships:
            if i == 9:
                new_line += '\n    ' + ('⎯' * 40) + \
                            '\n' + ' ' + '10' + ' | '
            else:
                new_line += '\n    ' + ('⎯' * 40) + \
                            '\n' + '  ' + str(i + 1) + ' | '
            for each in row:
                tmp = each.get_char((i, j))
                if tmp == chars.SHIP_AREA:
                    tmp = chars.EMPTY_AREA
                new_line += tmp + ' | '
                j += 1
            j = 0
            i += 1
        new_line += ('\n    ' + '⎯' * 40) + '\n'
        return new_line

    def field_with_ships(self):
        """
        Method to print field with all ships viewed
        :return :string, needed field
        """
        new_line = ''
        i, j = 0, 0
        line = 'ABCDEFGHIJ'
        new_line += '\n    | ' + ' | '.join(line) + ' |'
        for row in self.ships:
            if i == 9:
                new_line += '\n    ' + ('⎯' * 40) + \
                            '\n' + ' ' + '10' + ' | '
            else:
                new_line += '\n    ' + ('⎯' * 40) + \
                            '\n' + '  ' + str(i + 1) + ' | '
            for each in row:
                new_line += each.get_char((i, j)) + ' | '
                j += 1
            j = 0
            i += 1
        new_line += ('\n    ' + '⎯' * 40) + '\n'
        return new_line

    def add_ship(self, ship):
        """
        Method to add ship on the playing field. add Warning ships and
        needed ship on the field.
        :param ship: Ship instance
        """
        for i in range(ship.bow[0] - 1, ship.bow[0] + ship.length[0] + 1):
            for j in range(ship.bow[1] - 1, ship.bow[1] + ship.length[1] + 1):
                if i in range(0, 10) and j in range(0, 10):
                    self.ships[i][j] = WarningDeck((i, j))
        for i in range(ship.length[0]):
            for j in range(ship.length[1]):
                self.ships[i + ship.bow[0]][j + ship.bow[1]] = ship

    def is_valid(self, ship):
        """
        check if it is valid to situate ship here or not
        :param ship: Ship instance
        :return: True if possible, False if not
        """
        for i in range(ship.length[0]):
            for j in range(ship.length[1]):
                if isinstance(
                        self.ships[i + ship.bow[0]][j + ship.bow[1]],
                        WarningDeck) \
                        or isinstance(
                        self.ships[i + ship.bow[0]][j + ship.bow[1]],
                        FourDeck) \
                        or isinstance(
                        self.ships[i + ship.bow[0]][j + ship.bow[1]],
                        ThreeDeck) \
                        or isinstance(
                        self.ships[i + ship.bow[0]][j + ship.bow[1]],
                        TwoDeck) \
                        or isinstance(
                        self.ships[i + ship.bow[0]][j + ship.bow[1]],
                        OneDeck):
                    return False
        return True
