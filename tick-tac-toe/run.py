from tic_tac_toe import TicTacToe
from player import HumanPlayer, EasyComputerPlayer


def run():
    """ Tic-Tac-Toe. """
    run = TicTacToe()

    player_x = HumanPlayer('X')
    player_o = EasyComputerPlayer('O')

    # Starting the game.
    run.start_game(run, player_x, player_o, print_game=True)


if __name__ == '__main__':
    run()
