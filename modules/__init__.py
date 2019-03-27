from modules.field import *
from modules.ship import *
from modules.player import *
from modules.game import *
from modules.chars import *
from modules.exceptions import *

import random


def create_field():
    ships = [[EmptyDeck((i, j)) for i in range(10)] for j in range(10)]
    field = Field(ships)
    num_of_ships = 0
    current_ship = 4
    while num_of_ships < 10:
        horizontal = random.randint(0, 1)
        if horizontal:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - current_ship)
        else:
            x = random.randint(0, 9 - current_ship)
            y = random.randint(0, 9)
        if current_ship == 4:
            deck = FourDeck((x, y), horizontal)
        elif current_ship == 3:
            deck = ThreeDeck((x, y), horizontal)
        elif current_ship == 2:
            deck = TwoDeck((x, y), horizontal)
        else:
            deck = OneDeck((x, y))

        if field.is_valid(deck):
            field.add_ship(deck)
            num_of_ships += 1
            if num_of_ships == 1:
                current_ship -= 1
            elif num_of_ships == 3:
                current_ship -= 1
            elif num_of_ships == 6:
                current_ship -= 1
        else:
            continue
    return field


# field = create_field()

# print(field.field_with_ships())
# field.shoot_at((0, 0))
# field.shoot_at((1, 1))
# field.shoot_at((2, 2))
# field.shoot_at((3, 3))
# field.shoot_at((4, 4))
# field.shoot_at((5, 5))
# field.shoot_at((6, 6))
# print(field.field_with_ships())
# print(field.field_without_ships())