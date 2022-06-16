from tic_tac_toe import TicTacToe
from player import HumanPlayer, EasyComputerPlayer


def run():
    """ Tic-Tac-Toe. """
    run = TicTacToe()

    player_x = HumanPlayer('X')
    player_o = EasyComputerPlayer('O')

    while True:
        start = TicTacToe()
        # Starting the game.
        run.start_game(start, player_x, player_o, print_game=True)
        # Requesting user input.
        run.restart()

        continue


if __name__ == '__main__':
    run()
