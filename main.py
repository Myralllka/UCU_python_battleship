#!/bin/env ipython

from modules import *

import getpass


if __name__ == '__main__':

    authenticator = Authenticator()
    authorizer = Authorizer(authenticator)
    authenticator.sign_up('root', 'password1')
    authenticator.login('root', 'password1')
    authorizer.add_permission("watch1")
    authorizer.add_permission("watch2")
    authorizer.permit_user('root', "watch1")
    authorizer.permit_user('root', "watch2")

    players = []
    player = 0
    while player != 2:

        try:
            print(players)
            players.append(input('Player %s: ' % str(player + 1)))
            pas = getpass.getpass()
            authenticator.sign_up(players[player], pas)
            authenticator.login(players[player], pas)
            authorizer.permit_user(players[player],
                                   'watch%s' % str(player + 1))
            player += 1
        except AuthException as e:
            print(e)
            players.remove(players[-1])

    field1 = create_field()
    field2 = create_field()
    player1 = authenticator.users[players[0]]
    player2 = authenticator.users[players[1]]
    game = Game([field1, field2], [player1, player2])
    winner = ''
    print(
            "\n\n\nHello, player one ({}) and player two ({})! You start to play in "
            "the BattleShip game. You need to shoot in a right way, input"
            "letter and value without spaces, for example A1 or B10. EOF to "
            "see your board (Ctrl + d)"
                .format(player1.name, player2.name))
    input('press eny key to continue: ')
    while True:
        try:
            missed = True
            enemy = -1 * game.current_player + 1
            permission = 'watch%s' % str(game.current_player + 1)
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
            try:
                login = game.players[game.current_player].name
                print()
                pas = getpass.getpass()
                if authorizer.check_permission(login, permission) and \
                        (authenticator.users[login].check_password(pas)):
                    print(game.fields[
                                  game.current_player].field_with_ships())
                    input('press eny key to continue: ')
            except IncorrectPassword as e:
                print(e)
        except AssertionError:
            print('incorrect input. try again!')
        except ValueError:
            print('incorrect input. try again!')

    print("Congratulations! {} Win!".format(winner))
