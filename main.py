#!/bin/env python3

from modules import *

player1 = Player(input('please, input here first player name > '))
player2 = Player(input('please, input here second player name > '))
field1 = create_field()
field2 = create_field()

game = Game([field1, field2], [player1, player2])
winner = ''
print("\n\n\nHello, player one ({}) and player two ({})! You start to play in "
      "the BattleShip game. You need to shoot in a right way, input"
      "letter and value without spaces, for example A1 or B10. EOF to "
      "see your board (Ctrl + d)"
      .format(player1.name, player2.name))
input('press eny key to continue: ')
while True:
    try:
        missed = True
        enemy = -1 * game.current_player + 1
        print(game.fields[enemy].field_without_ships())
        coordinates = game.read_position()
        if game.fields[enemy].shoot_at(coordinates):
            print("You are grate!")
            missed = False
        else:
            print("You miss!")
        if game.is_end():
            winner = game.players[game.current_player].name
            break
        if missed:
            game.current_player = enemy
    except EOFError:
        print(game.fields[game.current_player].field_with_ships())
        input('press eny key to continue: ')
    except AssertionError:
        print('incorrect input. try again!')

print("Congratulations! {} Win!".format(winner))
