import time

from tic_tac_toe import TicTacToe
from player import HumanPlayer, EasyComputerPlayer


def start_game(game, x_player, o_player, print_game=True):
    """ Start game with x_player and o_player. """

    if print_game:
        print()
        game.display_board_numbers()

    # Starting letter.
    letter = 'X'

    while game.empty_squares():
        # Selecting appropriate player.
        if letter == 'O':
            square = o_player.move(game)
        else:
            square = x_player.move(game)

        # Function to make a move.
        if game.valid_move(square, letter):
            if print_game:
                print(f"\n{letter} makes a move to square {square}\n")
                game.display_board_numbers()
                print("-------------")
                game.display_board()

            if game.current_winner:
                if print_game:
                    print(f"\n{letter} Wins!")
                return letter

            # Switching players.
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.5)

    if print_game:
        print("\nTie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = EasyComputerPlayer('O')
    start = TicTacToe()
    start_game(start, x_player, o_player, print_game=True)
